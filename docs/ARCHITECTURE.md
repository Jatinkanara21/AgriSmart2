# AgriSmart Architecture

## Request flow

Flutter / React
        |
        v
     FastAPI
        |
  +-----+-----+---------+
  |           |         |
PostgreSQL   ML       External APIs
             |
       Crop / Disease / Yield
             |
          AgriBot

## Development order

1. Repository foundation
2. FastAPI backend skeleton
3. PostgreSQL schema
4. Authentication
5. Crop recommendation
6. Disease detection
7. Yield prediction
8. AgriBot
9. Flutter application
10. Admin dashboard
11. Testing and deployment
