---
termino: Model Context Protocol
alias: MCP o protocolo de contexto de modelo
slug: model-context-protocol
categorias: [tecnico, datos]
relacionados: [ia-agentica, ingenieria-de-contexto, prompt-injection, responsable-del-tratamiento]
actualizado: 2026-08-31
estado: publicado
---

Estándar abierto que normaliza cómo una aplicación de IA se conecta a sistemas externos —archivos, bases de datos, buscadores, servicios de terceros— para consultarlos y actuar sobre ellos sin programar una integración a medida para cada uno; [su documentación](https://modelcontextprotocol.io/docs/getting-started/intro) lo compara con un puerto USB-C para aplicaciones de IA. Lo publicó Anthropic en noviembre de 2024 y [lo donó el 9 de diciembre de 2025](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) a la Agentic AI Foundation de la Linux Foundation, con OpenAI y Block como cofundadores. Es hoy la forma habitual de dar herramientas a un agente, y por eso empieza a aparecer en los contratos.

Su interés jurídico está en que convierte una decisión de producto en un flujo de datos. Cada servidor MCP que se enchufa al asistente de una empresa y accede a datos personales por cuenta de esta es un encargado del tratamiento: el artículo 28.1 del [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02016R0679-20160504) obliga a elegir únicamente a quien ofrezca «garantías suficientes», y el 28.3, a regir la relación por contrato con instrucciones documentadas. Instalar un conector lleva un minuto; la diligencia del artículo 28, no.

El segundo frente es la seguridad. Lo que un servidor devuelve entra en la ventana de contexto y el modelo puede leerlo como instrucción, de modo que MCP extiende la superficie de la inyección de instrucciones a cualquier documento o página que el agente consulte; el [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) cataloga los riesgos propios del protocolo —envenenamiento de herramientas, mala gestión de credenciales, servidores no inventariados—. En un despacho el problema se agudiza: conectar el gestor de expedientes a un agente introduce material amparado por el deber de secreto del artículo 542.3 de la [Ley Orgánica del Poder Judicial](https://www.boe.es/buscar/act.php?id=BOE-A-1985-12666) en un canal que hay que poder auditar después, justo lo que la AEPD reclama en sus [orientaciones sobre IA agéntica](https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-agencia-publica-unas-orientaciones-sobre-inteligencia) al pedir limitar el acceso a lo estrictamente necesario y registrar lo que el agente hace.
