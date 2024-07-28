import mysql.connector
import logging


####CREATE COMMANDS

def create_table_invoices(db_user, db_password, db_host, db_name):

    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS invoices (
            entity_name VARCHAR(255) NOT NULL,
            entity_address_city VARCHAR(255),
            entity_country VARCHAR(255) NOT NULL,
            entity_id FLOAT,
            entity_type VARCHAR(255),
            item_code VARCHAR(255),
            item_name VARCHAR(255) NOT NULL,
            item_measure VARCHAR(255),
            item_qty FLOAT NOT NULL,
            item_gross_price FLOAT NOT NULL,
            invoice_id BIGINT NOT NULL,
            date DATE NOT NULL,
            amount_gross DECIMAL(15, 2) NOT NULL,
            currency VARCHAR(10) NOT NULL,
            Product_Reference VARCHAR(255),
            Product_Category VARCHAR(255),
            first_sale DATE NOT NULL
        );
        """
        logging.info('Executing query to create table')
        cursor.execute(create_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        logging.info('Table created successfully')
        return 'Table created successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)


def create_table_margins_month_year(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS margins_month_year (
            month_year DATE NOT NULL,
            total_invoices_amount_gross FLOAT NOT NULL,
            total_expenses_amount_gross FLOAT NOT NULL,
            Margins FLOAT NOT NULL,
            label VARCHAR(10) NOT NULL
        );
        """
        logging.info('Executing query to create table')
        cursor.execute(create_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        logging.info('Table created successfully')
        return 'Table created successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)


def create_table_expenses(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS expenses (
            entity_name VARCHAR(255) NOT NULL,
            entity_address_city VARCHAR(255),
            entity_country VARCHAR(255) NOT NULL,
            entity_id FLOAT,
            entity_type VARCHAR(255),
            item_code VARCHAR(255),
            item_name VARCHAR(255) NOT NULL,
            item_measure VARCHAR(255),
            item_qty FLOAT NOT NULL,
            item_gross_price FLOAT NOT NULL,
            invoice_id BIGINT NOT NULL,
            date DATE NOT NULL,
            amount_gross DECIMAL(15, 2) NOT NULL,
            currency VARCHAR(10) NOT NULL
        );
        """
        logging.info('Executing query to create table')
        cursor.execute(create_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        logging.info('Table created successfully')
        return 'Table created successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)


def create_tables_for_RFM_segmentation(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        create_table_queries = [
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(255) NOT NULL,
                Recency INT NOT NULL,
                Frequency INT NOT NULL,
                Monetary DECIMAL(15, 2) NOT NULL,
                R CHAR(1) NOT NULL,
                F CHAR(1) NOT NULL,
                M CHAR(1) NOT NULL,
                RFM_Segment VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS brackets_monetary_df (
                M_Value INT NOT NULL,
                Bins_Edges VARCHAR(255) NOT NULL,
                Quantile_Range VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS brackets_recency_df (
                R_Value INT NOT NULL,
                Bins_Edges VARCHAR(255) NOT NULL,
                Probabilities_of_ordering_again VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS brackets_frequency_df (
                F_Value INT NOT NULL,
                Bins_Edges VARCHAR(255) NOT NULL,
                Quantile_Range VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS segments_df (
                Segment VARCHAR(255) NOT NULL,
                R_Value INT NOT NULL,
                F_Value_Range VARCHAR(50) NOT NULL,
                M_Value_Range VARCHAR(50) NOT NULL
            );
            """
        ]

        for query in create_table_queries:
            logging.info('Executing query to create table')
            cursor.execute(query)
            conn.commit()

        cursor.close()
        conn.close()

        logging.info('Tables created successfully')
        return 'Tables created successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)

####DELETE COMMANDS

def delete_tables_for_RFM_segmentation(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        delete_table_queries = [
            "DROP TABLE IF EXISTS customers;",
            "DROP TABLE IF EXISTS brackets_monetary_df;",
            "DROP TABLE IF EXISTS brackets_recency_df;",
            "DROP TABLE IF EXISTS brackets_frequency_df;",
            "DROP TABLE IF EXISTS segments_df;"
        ]

        for query in delete_table_queries:
            logging.info('Executing query to delete table')
            cursor.execute(query)
            conn.commit()

        cursor.close()
        conn.close()

        logging.info('Tables deleted successfully')
        return 'Tables deleted successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)


def delete_table_margins_month_year(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        delete_table_query = "DROP TABLE IF EXISTS margins_month_year;"
        logging.info('Executing query to delete table')
        cursor.execute(delete_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        logging.info('Table deleted successfully')
        return 'Table deleted successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)


def delete_table_invoices(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        delete_table_query = "DROP TABLE IF EXISTS invoices;"
        logging.info('Executing query to delete table')
        cursor.execute(delete_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        logging.info('Table deleted successfully')
        return 'Table deleted successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)

def delete_table_expenses(db_user, db_password, db_host, db_name):
    logging.info('Function execution started')

    try:
        logging.info('Attempting to connect to the database')
        conn = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        logging.info('Connection successful')
        cursor = conn.cursor()

        delete_table_query = "DROP TABLE IF EXISTS expenses;"
        logging.info('Executing query to delete table')
        cursor.execute(delete_table_query)
        conn.commit()

        cursor.close()
        conn.close()

        logging.info('Table deleted successfully')
        return 'Table deleted successfully'

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return str(e)


#####APPEND COMMANDS

def append_data_invoices_and_expenses_update_data_rfm(db_user, db_password, db_host, db_name):
    logging.info('append_data endpoint called')

    # Generate the df_rfm and df_invoices DataFrames
    df_invoices, expense, df_rfm, brackets_recency_df, brackets_frequency_df, brackets_monetary_df, segments_df, margins_month_year = generate_rfm_tables_and_df_invoices_and_expenses()

    
    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')
    logging.info('SQLAlchemy engine created')

    try:
        # Append df_rfm to the 'customers' table
        logging.info('Attempting to append df_rfm data to the customers table')
        df_rfm.to_sql('customers', con=engine, if_exists='append', index=False)
        logging.info('df_rfm data appended successfully')

        # Append df_invoices to the 'invoices' table
        logging.info('Attempting to append df_invoices data to the invoices table')
        df_invoices.to_sql('invoices', con=engine, if_exists='append', index=False)
        logging.info('df_invoices data appended successfully')

        # Append expense to the 'expenses' table
        logging.info('Attempting to append expense data to the expenses table')
        expense.to_sql('expenses', con=engine, if_exists='append', index=False)
        logging.info('df_invoices data appended successfully')

        # Append brackets_recency_df to the 'brackets_recency_df' table
        logging.info('Attempting to append churning_brackets data to the invoices table')
        brackets_recency_df.to_sql('brackets_recency_df', con=engine, if_exists='append', index=False)
        logging.info('churning_brackets data appended successfully')

        # Append brackets_frequency_df to the 'brackets_frequency_df' table
        logging.info('Attempting to append churning_brackets data to the invoices table')
        brackets_frequency_df.to_sql('brackets_frequency_df', con=engine, if_exists='append', index=False)
        logging.info('churning_brackets data appended successfully')

        # Append brackets_monetary_df to the 'brackets_monetary_df' table
        logging.info('Attempting to append churning_brackets data to the invoices table')
        brackets_monetary_df.to_sql('brackets_monetary_df', con=engine, if_exists='append', index=False)
        logging.info('churning_brackets data appended successfully')

        # Append segments_df to the 'segments_df' table
        logging.info('Attempting to append churning_brackets data to the invoices table')
        segments_df.to_sql('segments_df', con=engine, if_exists='append', index=False)
        logging.info('churning_brackets data appended successfully')

        # Append margins_month_year to the 'margins_month_year' table
        logging.info('Attempting to append margins_month_year data to the invoices table')
        margins_month_year.to_sql('margins_month_year', con=engine, if_exists='append', index=False)
        logging.info('margins_month_year data appended successfully')

        return 'Data appended successfully'

    except Exception as e:
        logging.error(f'Error occurred while appending data: {str(e)}')
        return str(e)

    finally:
        engine.dispose()
        logging.info('SQLAlchemy engine disposed')
