# CyrptoBot_with_Binance_Project

Step 1 : Collecting the data

        Goal
        - Collecting two types of data through the Binance API using a streaming architecture
        - We can retrieve information on the prices of different markets (BTC-USDT, BTC-ETH, ...).
        - The goal will be to create a generic data retrieval function in order to have data from any market.
        - It will also be necessary to create a pre-processing script to reorganise the data coming out of the stream so that it is clean.
        - Recovering historical data, pre-processed to train our future model

        Modules
        - 

        Condtion of Validation
        - Treatment explanation file (doc / pdf)
        - JSON file of the data

Step 2 : Data modeling

        Goal
        It is a question of choosing the most suitable storage solution.
        - 2 SQL tables, one for historical data and one for streaming data
        - A Mongo/Elastic DB with 2 collections: one for stream data and one for data

        Modules
        142 - SQL
        Elasticsearch
        143 - MongoDB

        Condtion of Validation
        - A relational database UML Diagram 
        - A file who creates and queries the SQL database.
        - Same files for a Elastic/Mongo/ DataBase
