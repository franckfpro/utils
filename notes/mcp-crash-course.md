---
title: "MCP (Model Context Protocol) : Architecture, Serveur Custom et Orchestration Multi-Agents"
aliases:
  - Model Context Protocol Tutorial
  - MCP Crash Course
tags:
  - ai/mcp
  - architecture/agents
  - dev/typescript
  - automation/workflows
  - security/ai
source: "https://www.youtube.com/watch?v=PjYcrCEzV6M"
channel: "Traversy Media"
date_created: 2026-11-22
status: evergreen
---

# MCP (Model Context Protocol) : Architecture, Serveur Custom et Orchestration Multi-Agents

> [!abstract] Concept Clé (Note Atomique)
> Le **Model Context Protocol (MCP)** est un protocole standardisé qui agit comme un **hub USB universel** entre un hôte IA (Client : Claude Code, Codex, Cursor) et des services externes (Serveurs MCP). Il remplace les intégrations ad hoc par un contrat client-serveur unifié permettant la découverte dynamique et l'exécution de **Tools**, **Resources** et **Prompts** [00:00:17, 00:03:53, 00:04:26].

---

## 1. Architecture et Fondamentaux

### Le Modèle Client-Hôte-Serveur
* **Host (Hôte)** : L'application IA qui héberge le modèle (ex. Claude Desktop, Claude Code CLI, Codex, Cursor) [00:04:07].
* **MCP Server (Serveur)** : Le pont exposé par un service ou une application locale qui déclare ses capacités [00:04:19, 00:04:26].
* **Flux de contrôle** : Le modèle de langage **ne communique jamais directement** avec le serveur MCP. Il formule une intention d'appel d'outil auprès de l'Hôte, qui demande validation à l'utilisateur (selon les permissions) et exécute la requête [00:05:03].

### Anatomie d'un Tool MCP
Un outil est une fonction exposée côté serveur définie par trois éléments indispensables pour le LLM [00:04:46, 00:04:51] :
1. **Name / Title** : Identifiant unique de l'action.
2. **Description** : Contexte sémantique expliquant au modèle *quand* et *pourquoi* utiliser l'outil.
3. **Input Schema** : Validation stricte des paramètres attendus (généralement via `Zod` en TypeScript) [00:04:51, 00:10:04].

---

## 2. Configuration, Transports et Portées (Scopes)

### Méthodes de Transport
* **Local (`stdio`)** : Communication via entrée/sortie standard pour des processus tournant sur la machine locale [00:07:11].
* **Distant (`http`)** : Communication réseau vers des serveurs distants (souvent couplée à une authentification OAuth) [00:06:07, 00:07:19].

### Gestion des Scopes (Claude Code)
La portée détermine l'accessibilité du serveur MCP [00:07:36] :

| Scope                  | Visibilité                                         | Stockage / Mécanisme                                | Cas d'usage                                                  |
| :--------------------- | :------------------------------------------------- | :-------------------------------------------------- | :----------------------------------------------------------- |
| **`local`** *(défaut)* | Utilisateur uniquement, dossier courant uniquement | Configuration locale privée                         | Tests, serveurs spécifiques à un projet [00:07:50]           |
| **`user`**             | Utilisateur uniquement, tous les projets           | Configuration globale machine                       | Outils personnels transverses (ex. Notion, Apify) [00:08:07] |
| **`project`**          | Toute l'équipe sur le dépôt                        | Fichier `.mcp.json` à la racine (versionné via Git) | Standardisation de l'environnement d'équipe [00:08:27]       |

> [!tip] Connectors vs Plugins
> Dans les interfaces graphiques (Claude Desktop/Web), les **Connectors** sont des serveurs MCP hébergés avec authentification OAuth intégrée, tandis que les **Plugins** sont des paquets complets regroupant serveurs MCP, *Skills* et configurations [00:06:01, 00:06:07].

---

## 3. Tutoriel Avancé : Créer un Serveur MCP Local en TypeScript

Implémentation d'un serveur `order-status-server` permettant d'interroger un fichier local `orders.json` via le SDK officiel `@modelcontextprotocol/sdk` [00:09:16, 00:09:32].

### Étape 1 : Code du Serveur (`index.ts`)
Le serveur initialise l'instance `McpServer`, enregistre les outils avec validation `Zod` et écoute sur `StdioServerTransport` [00:09:41, 00:10:04] :

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { getOrderStatusById, getAllOrders, formatOrder } from "./orders.js";

// 1. Initialisation du serveur MCP
const server = new McpServer({
  name: "order-status-server",
  version: "1.0.0",
});

// 2. Enregistrement d'un outil avec paramètres (Input Schema)
server.registerTool(
  "get_order_status",
  {
    title: "Get Order Status",
    description: "Récupère le statut d'une commande spécifique via son identifiant.",
    inputSchema: {
      orderId: z.string().describe("L'identifiant unique de la commande (ex: order-2)"),
    },
  },
  async ({ orderId }) => {
    const order = await getOrderStatusById(orderId);
    if (!order) {
      return {
        content: [{ type: "text", text: `Commande ${orderId} introuvable.` }],
      };
    }
    return {
      content: [{ type: "text", text: formatOrder(order) }],
    };
  }
);

// 3. Enregistrement d'un outil sans paramètres
server.registerTool(
  "get_all_orders",
  {
    title: "Get All Orders",
    description: "Liste l'ensemble des commandes disponibles.",
  },
  async () => {
    const orders = await getAllOrders();
    return {
      content: [{ type: "text", text: JSON.stringify(orders, null, 2) }],
    };
  }
);

// 4. Connexion au transport Standard I/O
const transport = new StdioServerTransport();
await server.connect(transport);

```

### Étape 2 : Enregistrement dans Claude Code CLI

Utilisation de l'option `--silent` sur `npm` pour éviter que les logs de démarrage ne corrompent le flux JSON du protocole `stdio` [00:12:56] :

```bash
claude mcp add \
  --transport stdio \
  --scope local \
  order-status-server \
  -- npm --prefix /chemin/vers/mcp-order-status-dev --silent run dev

```

*Note : Redémarrer le client après l'ajout pour charger le catalogue d'outils [00:13:12].*

---

## 4. Orchestration Multi-MCP : Workflow de Prospection Automatisé

Démonstration d'une chaîne d'exécution coordonnant deux serveurs MCP distants (**Apify** pour l'extraction web et **Notion** pour le stockage structuré) [00:02:10, 00:02:40].

### Phase 1 : Connexion et Authentification

1. **Ajout du serveur Apify (HTTP / Scope User)** [00:17:58] :
```bash
claude mcp add --transport http --scope user apify [https://mcp.apify.com](https://mcp.apify.com)

```


2. **Authentification OAuth** : Dans le client, exécuter `/mcp`, sélectionner le serveur marqué d'un `!` et valider les permissions OAuth dans le navigateur [00:18:33, 00:18:47].
3. **Ajout de Notion** : Via le catalogue de *Connectors* intégrés ou via la commande CLI équivalente [00:24:39, 00:24:45].

### Phase 2 : Découverte et Inspection d'Acteurs (Apify)

Avant d'exécuter un scraping coûteux, l'agent inspecte le catalogue d'outils (*Actors*) et leur schéma d'entrée [00:20:50, 00:21:11] :

* **Outil appelé** : Recherche dans le store Apify → sélection de `Google Maps Scraper` [00:21:11, 00:21:34].
* **Validation** : Vérification du coût estimé et des paramètres avant exécution [00:21:54].

### Phase 3 : Extraction et Filtrage Intelligent

* **Exécution** : L'agent appelle `apify:call-actor` pour extraire 5 agences web à Boston [00:22:27, 00:23:14, 00:24:00].
* **Curation par l'agent** : L'IA détecte qu'un résultat (*Websites USA*) est une firme nationale avec une page locale et propose de le remplacer par une véritable agence locale avant de valider le dataset [00:23:41].

### Phase 4 : Persistance dans Notion

* **Action** : L'agent utilise le MCP Notion pour créer une base de données `Boston Web Development Agencies` et insérer chaque enregistrement (Nom, Catégorie, URL Maps, Téléphone, Email) [00:26:02, 00:26:48].

### Phase 5 : Enrichissement via RAG Web Browser

Pour analyser en profondeur une agence sans consommer excessivement de tokens via un navigateur classique (captures d'écran multiples) [00:27:26, 00:27:42] :

1. **Appel de `RAG Web Browser` (Apify)** : Exécute une recherche `site:letsdesignyoursite.com`, extrait le contenu *headless* côté serveur et nettoie le HTML (suppression des menus/footers) pour ne renvoyer que du texte brut structuré [00:27:50, 00:28:44].
2. **Mise à jour Notion** : L'agent synthétise un brief (services, activité récente) et met à jour la ligne correspondante dans la base Notion [00:30:51, 00:31:57].

---

## 5. Sécurité et Limites Architecturales

> [!danger] Risque Critique : Supply Chain Attack (Cas `postmark-mcp`)
> * **L'incident** : Un acteur malveillant a publié sur npm un paquet nommé `postmark-mcp` copiant le serveur officiel de Postmark [00:32:24, 00:32:42].
> * **Le mécanisme** : Légitime pendant 15 versions, la version `1.0.16` a introduit une ligne ajoutant l'attaquant en copie cachée (**BCC**) sur chaque email envoyé par l'agent (factures, réinitialisations de mots de passe) [00:32:48, 00:32:57].
> * **Règle d'hygiène** : Ne jamais installer un MCP trouvé au hasard sur Google. Toujours vérifier la source officielle (documentation éditeur, dépôt GitHub vérifié ou *Connectors* officiels) et auditer les permissions demandées [00:33:12, 00:33:17].

### Quand NE PAS utiliser MCP ?

Le protocole MCP ajoute de la configuration, des dépendances et de la latence [00:33:37].

* **Éviter MCP** : Dans une application logicielle classique où vous contrôlez les deux extrémités avec une intégration fixe (un simple appel API REST ou une fonction native est plus rapide et robuste) [00:33:46].
* **Privilégier MCP** : Lorsqu'un hôte IA autonome doit **découvrir dynamiquement** et **orchestrer** des capacités hétérogènes à travers plusieurs outils ou services externes [00:34:03].

---

## Liens Connexes (Zettelkasten)

* [[Architecture des Agents IA]]
* [[Sécurité des LLM et Prompt Injection]]
* [[Retrieval-Augmented Generation (RAG)]]
* [[SDK TypeScript et Validation Zod]]

