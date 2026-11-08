**Desarrollo — 8 noviembre:** General original en español, Teclado y Pantalla con páginas internas y retornos nativos a Home comprobados en overlays separados. Límite de suscripciones D-Bus restaurado al valor OEM; recursos y espera EGL todavía pendientes. El perfil Windows aceptado se conserva; no se prepara v2. [Evidencia de desarrollo](PROGRESS-2026-11-08-SETTINGS-GENERAL-SPANISH.md). La tabla inferior sigue describiendo el producto aceptado anterior, no una promoción de estos proveedores.

Actualización de Ajustes: Sonido y Ecualizador originales visibles con ratón en desarrollo separado; destino completo y retorno nativo a Home comprobados; español y recursos pendientes. No clasificar como integrado. [Resultado nuevo](PROGRESS-2026-11-07-SETTINGS-PERSISTENCE.md).

# Disponibilidad del entorno integrado

Resultados del perfil BC3N25MY, offline, con país Europa y español EU. La tabla diferencia vistas lógicas del mismo Home y ejecutables independientes. Los resultados previos de perfiles separados se conservan y no se extrapolan.

| Aplicación/vista | Estado integrado | Resultado y límite |
| --- | --- | --- |
| Home (11) | Navegable | Pantalla original completa, arrastre y menús por ratón; alguna textura fuera del conjunto observado sigue ausente. |
| N Mode (500) | Navegable | Vista original Track dentro de Home, ceros/OFF nativos, entrada y vuelta a Home. No telemetría ni cambios del vehículo. |
| Manual | Navegable | Vista original española dentro de Home, QR/texto y Atrás. No se abrió el enlace web ni se afirma manual completo offline. |
| Radio (77) | Navegable (UI) | FM original visible, 0.0 MHz/sin sintonizador. Regreso con el botón Home tras dibujo completo comprobado en las sesiones integradas. Otro recorrido dejó Home sin buffer; no se generaliza a todas las secuencias. No audio/RF probado. |
| Ajustes / AppSetup (60) | Parcial | Raíz de Home visible; proveedor original registrado, superficie oculta/sin buffer y posterior terminación ordenada por AppManager. Sonido no mostró contenido. |
| Medios / AppMediaPlayer (100) | Parcial | Proveedor original vivo/registrado con runtime OEM TSE verificado; el icono no mostró interfaz nueva. No fuentes conectadas. |
| Nota de voz (117) | Parcial | El perfil anterior sí mostró la lista vacía; el integrado 81/high1 no mostró contenido. No micrófono/grabación. |
| Teléfono (121) | Sin hardware | Sin Bluetooth/smartphone; no se repitió su inicialización fallida anterior. No se atribuye todo su fallo al hardware sin evidencia. |
| Proyección | Sin hardware | Sin smartphone. El clic no abrió otra UI; no se inventa un popup ni una conexión. |
| Climatización (13) | Ausente | Ejecutable ausente en la base inspeccionada; un icono no demuestra aplicación disponible. Tampoco hay climatizador físico. |
| Modo silencioso | Sin hardware | No accionado: sin altavoces/ocupantes reales. |
| Navegación (30) | Ausente | Ejecutable ausente en el montaje actual. Recuperación del host separada; mapas, licencias y montaje por verificar. |
| Actualización / flasheo / ingeniería / diagnóstico / eCall | Excluida por seguridad | No se ejecutan. Los servicios internos no se cuentan como aplicaciones gráficas. |

El arranque opcional de proveedores de Ajustes/Medios coincidió con textos cambiados a inglés pese a argumentos `-l:7`. La causa exacta no está aislada; estos proveedores no se precargan en el perfil de uso del propietario. La VM/overlay experimental es independiente y conserva evidencias privadas.

El inventario estático completo contiene 35 entradas Launcher y 154 entradas lógicas del gestor; **no equivalen a 189 aplicaciones independientes ni verificadas**. La ronda integrada recorre varios iconos consecutivamente en una sola VM y continúa cuando uno falla. No promete navegación, audio, servicios móviles ni el sistema completo. [Lanzador Windows](WINDOWS-LAUNCHER.md) · [Evidencia integrada](PROGRESS-2026-11-07-WINDOWS-PRODUCT.md).
