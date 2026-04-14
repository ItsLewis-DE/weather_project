{{ config(
    materialized = 'table',
    unique_key='id'
)}}
select 
    city,
    temperature,
    wind_speed,
    weather_time_local
FROM {{ ref('staging') }}