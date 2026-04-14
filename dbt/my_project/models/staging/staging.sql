{{ config(materialized='table', unique_key ='id')}}

with source as (
SELECT * 
from {{ source('dev', 'raw_weather_data') }}
),

de_dup AS (
    SELECT  *,
    row_number() OVER(PARTITION BY time ORDER BY inserted_at DESC) AS rn
    FROM source
)

SELECT 
    id,
    city,
    temperature,
    weather_description,
    wind_speed,
    time AS weather_time_local,
    (inserted_at +(utc_offet|| 'hours')::interval) AS inserted_at_utc
FROM de_dup
WHERE rn=1
