Projeto: Pipeline ETL com Python
Este projeto demonstra a implementação de um fluxo de ETL (Extract, Transform, Load), um dos pilares da Engenharia e Ciência de Dados. O objetivo é processar informações de clientes para gerar comunicações personalizadas de forma automatizada.

🛠️ O que acontece no código?
Extração (Extract): Simulamos o consumo de dados de clientes a partir de uma fonte de origem. Para garantir a resiliência e o funcionamento contínuo do projeto (independente de instabilidades em APIs externas), os dados foram estruturados diretamente em Python, representando o que seria extraído de um banco de dados ou arquivo CSV.

Transformação (Transform): Nesta etapa, aplicamos a lógica de negócio. O código analisa o perfil de cada cliente (como saldo e tipo de conta) e utiliza regras condicionais para criar mensagens personalizadas. É aqui que o dado bruto se transforma em informação útil para o marketing ou para a tomada de decisão.

Carregamento (Load): Os dados processados são preparados para o seu destino final. No projeto, os resultados são exibidos de forma estruturada, simulando o carregamento dessas informações em um novo banco de dados ou o envio para um sistema de notificações.

💡 Por que simular os dados?
Seguindo as orientações do desafio, a escolha por simular os dados em vez de depender exclusivamente de uma API externa foi estratégica. Isso demonstra adaptabilidade técnica: o código torna-se independente de terceiros, garantindo que o pipeline possa ser testado e demonstrado a qualquer momento, sem falhas de conexão.
