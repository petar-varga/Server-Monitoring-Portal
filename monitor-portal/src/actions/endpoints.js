export const LOGIN_API_PATH = "login/";
export const AUTH_USER_API_PATH = "auth_user";

export const SERVER_API_PATH = "server";
export const ALL_SERVERS_API_PATH = `${SERVER_API_PATH}/list`;
export const ADD_SERVER_API_PATH = `${SERVER_API_PATH}/add`;

export const MYSQL_QUERIES_API_PATH = "mysql-query";
export const ALL_MYSQL_QUERIES_API_PATH = `${MYSQL_QUERIES_API_PATH}/list/{}`;
export const ADD_MYSQL_QUERIES_API_PATH = `${MYSQL_QUERIES_API_PATH}/add`;

export const USERS_API_PATH = "users/";
export const USERS_DETAIL_API_PATH = `${USERS_API_PATH}{}/`;

export const AUCTIONS_API_PATH = "auctions/";
export const AUCTIONS_DETAIL_API_PATH = `${AUCTIONS_API_PATH}{}/`;
export const AUCTION_IMAGE_UPLOAD_API_PATH = `${AUCTIONS_API_PATH}upload_auction_image/`;

export const AUCTION_ITEMS_API_PATH = "auction_items/";
export const AUCTION_ITEM_DETAIL_API_PATH = `${AUCTION_ITEMS_API_PATH}{}/`;
export const AUCTION_ITEM_IMAGE_UPLOAD_API_PATH = `${AUCTION_ITEMS_API_PATH}upload_image/`;
export const AUCTION_ITEM_CUSTOMER_COLLECTIONS_SAVE_API_PATH = `${AUCTION_ITEM_DETAIL_API_PATH}save_customer_collections/`;

export const AUCTION_COLLECTIONS_API_PATH = "auction_collections/";
export const AUCTION_COLLECTION_DETAIL_API_PATH = `${AUCTION_COLLECTIONS_API_PATH}{}/`;
export const AUCTION_COLLECTION_IMAGE_UPLOAD_API_PATH = `${AUCTION_COLLECTIONS_API_PATH}upload_image/`;

export const JEWELRY_CLASSIFICATION_API_PATH = `jewelry_classification/`;
export const JEWELRY_CLASSIFICATION_DETAIL_API_PATH = `${JEWELRY_CLASSIFICATION_API_PATH}{}/`;
export const AUCTION_ITEMS_JEWELRY_LIST_API_PATH = `${JEWELRY_CLASSIFICATION_API_PATH}auction_item_jewelries`;
export const JEWELRY_CLASSIFICATION_ATTRIBUTE_API_PATH = `${JEWELRY_CLASSIFICATION_DETAIL_API_PATH}attributes/`;
export const JEWELRY_CLASSIFICATION_ADD_ATTRIBUTE_API_PATH = `${JEWELRY_CLASSIFICATION_DETAIL_API_PATH}add_attribute/`;
export const JEWELRY_CLASSIFICATION_ADD_ATTRIBUTE_DDL_VALUE_API_PATH = `${JEWELRY_CLASSIFICATION_DETAIL_API_PATH}add_attribute_ddl_value/`;

export const ITEM_SOURCES_API_PATH = "sources/";
export const ITEM_SOURCE_DETAIL_API_PATH = `${ITEM_SOURCES_API_PATH}{}/`;
export const ITEM_SOURCE_TYPES_API_PATH = `${ITEM_SOURCES_API_PATH}source_types/`;
export const ITEM_SOURCE_CUSTOMER_ITEMS_API_PATH = `${ITEM_SOURCES_API_PATH}customer_source_items/`;
export const ITEM_SOURCE_CUSTOMER_COLLECTIONS_API_PATH = `${ITEM_SOURCES_API_PATH}customer_collections/`;

export const AUCTION_TAGS_API_PATH = "auction_item_tags/";
export const AUCTION_TAG_DETAIL_API_PATH = `${AUCTION_TAGS_API_PATH}{}/`;
