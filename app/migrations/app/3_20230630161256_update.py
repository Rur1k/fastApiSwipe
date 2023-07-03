from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
    
    CREATE TABLE IF NOT EXISTS "house" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL UNIQUE,
    "district" VARCHAR(64),
    "micro_district" VARCHAR(64),
    "street" VARCHAR(64),
    "number" INT,
    "description" TEXT,
    "lcd_status" VARCHAR(64),
    "type_house" VARCHAR(64),
    "class_house" VARCHAR(64),
    "technologies" VARCHAR(64),
    "to_sea" VARCHAR(64),
    "payments" VARCHAR(64),
    "ceiling_height" VARCHAR(64),
    "gas" VARCHAR(64),
    "heating" VARCHAR(64),
    "sewerage" VARCHAR(64),
    "sales_dep_fullname" VARCHAR(128),
    "sales_dep_phone" VARCHAR(16),
    "sales_dep_email" VARCHAR(64),
    "registration" TEXT,
    "calculation_options" TEXT,
    "appointment" TEXT,
    "sum_in_contract" TEXT,
    "state" VARCHAR(64),
    "territory" VARCHAR(64),
    "maps" TEXT,
    "house_buildings" INT,
    "sections" INT,
    "floors" INT,
    "risers" INT,
    "builder_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);;
        CREATE TABLE IF NOT EXISTS "announcement" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "founding_documents" VARCHAR(64),
    "purpose" VARCHAR(64),
    "count_rooms" VARCHAR(64),
    "layout" VARCHAR(64),
    "residential_condition" VARCHAR(64),
    "all_square" DOUBLE PRECISION   DEFAULT 0,
    "balcony" BOOL   DEFAULT False,
    "heating_type" VARCHAR(64),
    "commission_to_agent" DOUBLE PRECISION   DEFAULT 0,
    "connection_type" VARCHAR(64),
    "description" TEXT,
    "price" DOUBLE PRECISION,
    "calculation_option" VARCHAR(64),
    "maps" TEXT,
    "pub_status" BOOL   DEFAULT False,
    "house_id" UUID REFERENCES "house" ("id") ON DELETE CASCADE,
    "user_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);;
        CREATE TABLE IF NOT EXISTS "favorite" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "announcement_id" UUID REFERENCES "announcement" ("id") ON DELETE CASCADE,
    "user_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);;
        CREATE TABLE IF NOT EXISTS "flat" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "number" INT,
    "count_room" INT,
    "square" DOUBLE PRECISION,
    "price_per_meter" DOUBLE PRECISION,
    "house_building" INT,
    "section" INT,
    "floor" INT,
    "riser" INT,
    "reserved" BOOL NOT NULL  DEFAULT False,
    "creator_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE,
    "house_id" UUID REFERENCES "house" ("id") ON DELETE CASCADE
);;
        CREATE TABLE IF NOT EXISTS "notary" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "first_name" VARCHAR(64),
    "last_name" VARCHAR(64),
    "phone" VARCHAR(16),
    "email" VARCHAR(64)
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "announcement";
        DROP TABLE IF EXISTS "favorite";
        DROP TABLE IF EXISTS "flat";
        DROP TABLE IF EXISTS "house";
        DROP TABLE IF EXISTS "notary";"""
