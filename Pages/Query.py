import streamlit as st
import pandas as pd
import mysql.connector as db

connection = db.connect(
      user = 'root',
      password = '123456789',
      host = '127.0.0.1',
      database = 'food_delivery'
)

cursor = connection.cursor()

st.title("Query View")


sql_queries = [
    "SELECT location AS Peak_Order_Locations FROM food_delivery.customers WHERE total_orders = (SELECT max(total_orders) FROM food_delivery.customers);",
    "SELECT preferred_cuisine, count(*) AS customer_count, sum(total_orders) AS most_ordered FROM food_delivery.customers GROUP BY preferred_cuisine ORDER BY most_ordered DESC;",
    "SELECT customer_id, count(*) AS total_orders FROM food_delivery.orders GROUP BY customer_id ORDER BY total_orders DESC;",
    "SELECT is_premium, AVG(total_orders) AS average_orders, AVG(average_rating) AS average_rating FROM food_delivery.customers GROUP BY is_premium;",
    "SELECT name, email, total_orders FROM food_delivery.customers WHERE total_orders > 5 ORDER BY total_orders DESC;",
    "SELECT average_rating, AVG(total_orders) as average_orders FROM food_delivery.customers GROUP BY average_rating ORDER BY average_rating DESC;",
    "SELECT is_premium, count(*) as customer_count, sum(total_orders) as total_orders FROM food_delivery.customers GROUP BY is_premium ORDER BY total_orders DESC;",
    "SELECT name, total_orders, average_rating FROM food_delivery.customers WHERE total_orders > 3 AND average_rating >= 4 ORDER BY total_orders DESC;",
    "SELECT name, sum(total_orders) AS orders_list FROM food_delivery.restaurants GROUP by name ORDER by orders_list DESC;",
    "SELECT extract(HOUR FROM order_date) as order_hour,count(*) as total_orders FROM food_delivery.orders GROUP BY extract(HOUR FROM order_date) ORDER BY total_orders DESC;",
    "SELECT city, COUNT(*) as customer_count FROM food_delivery.customers GROUP BY city ORDER BY customer_count DESC;",
    "SELECT status AS popular_status, count(*) as total_orders FROM food_delivery.orders GROUP BY status ORDER BY total_orders DESC;",
    "SELECT customer_id, count(*) AS total_orders FROM food_delivery.orders GROUP BY customer_id ORDER BY total_orders DESC;",
    "SELECT payment_mode, count(*) AS total_orders FROM food_delivery.orders GROUP BY payment_mode ORDER BY total_orders DESC;",
    "SELECT discount_applied, count(*) AS total_orders FROM food_delivery.orders GROUP BY discount_applied ORDER BY total_orders DESC;",
    "SELECT * FROM food_delivery.deliveries WHERE delivery_time > estimated_time AND delivery_status != 'Cancelled';",
    "SELECT rider_id, AVG(rating) as avg_rating FROM food_delivery.rider_reviews GROUP BY rider_id ORDER BY avg_rating DESC;",
    "SELECT vehicle_type, count(*) as Frequency FROM food_delivery.deliveries GROUP BY vehicle_type ORDER BY Frequency DESC;",
    "SELECT AVG(delivery_time) AS Average_Time_Taken FROM food_delivery.deliveries ORDER BY Average_Time_Taken;",
    "SELECT AVG(delivery_fee) AS Average_Delivery_Fee FROM food_delivery.deliveries ORDER BY Average_Delivery_Fee;",
    "SELECT AVG(distance) AS Average_Distance_Covered FROM food_delivery.deliveries ORDER BY Average_Distance_Covered;",
    "SELECT restaurant_id, AVG(preparation_time) as avg_prep_time FROM food_delivery.restaurants GROUP BY restaurant_id ORDER BY avg_prep_time;",
    "SELECT restaurant_id, COUNT(*) as order_count FROM food_delivery.orders GROUP BY restaurant_id ORDER BY order_count DESC;",
    "SELECT AVG(delivery_time) FROM food_delivery.deliveries WHERE vehicle_type = 'Bike';",
]

query_title = ["Peak Ordering Locations","Analyzing Customer Preferences","Top Customer Preferences","Customer Segmentation","Active Customers","Rating vs Orders","Customer Retention Patterns","High Value Customers","Frequent Restaurant Ordered","Peak Orderings of the Day",
               "Order Trends Over Time","Analyzing popular status","Top Customer Preferences","Top Payment Methods","Frequent Discount Usage","Tracking Delay Deliveries","Tracking Cancelled Deliveries","Frequent Vehicle Used for Delivery","Average Delivery Time","Average Delivery fee","Average Distance Covered"]

select_query = st.selectbox("Select A Query", query_title)

if select_query == "Peak Ordering Locations":
    cursor.execute(sql_queries[0])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[0], connection)
    st.dataframe(df)
elif select_query == "Analyzing Customer Preferences":
    cursor.execute(sql_queries[1])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[1], connection)
    st.dataframe(df)
elif select_query == "Top Customer Preferences":
    cursor.execute(sql_queries[2])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[2], connection)
    st.dataframe(df)
elif select_query == "Customer Segmentation":
    cursor.execute(sql_queries[3])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[3], connection)
    st.dataframe(df)
elif select_query == "Active Customers":
    cursor.execute(sql_queries[4])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[4], connection)
    st.dataframe(df)
elif select_query == "Rating vs Orders":
    cursor.execute(sql_queries[5])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[5], connection)
    st.dataframe(df)
elif select_query == "Customer Retention Patterns":
    cursor.execute(sql_queries[6])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[6], connection)
    st.dataframe(df)
elif select_query == "High Value Customers":
    cursor.execute(sql_queries[7])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[7], connection)
    st.dataframe(df)
elif select_query == "Frequent Restaurant Ordered":
    cursor.execute(sql_queries[8])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[8], connection)
    st.dataframe(df)
elif select_query == "Peak Orderings of the Day":
    cursor.execute(sql_queries[9])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[9], connection)
    st.dataframe(df)
elif select_query == "Order Trends Over Time":
    cursor.execute(sql_queries[10])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[10], connection)
    st.dataframe(df)
elif select_query == "Analyzing popular status":
    cursor.execute(sql_queries[11])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[11], connection)
    st.dataframe(df)
elif select_query == "Top Customer Preferences":
    cursor.execute(sql_queries[12])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[12], connection)
    st.dataframe(df)
elif select_query == "Top Payment Methods":
    cursor.execute(sql_queries[13])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[13], connection)
    st.dataframe(df)
elif select_query == "Frequent Discount Usage":
    cursor.execute(sql_queries[14])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[14], connection)
    st.dataframe(df)
elif select_query == "Tracking Delay Deliveries":
    cursor.execute(sql_queries[15])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[15], connection)
    st.dataframe(df)
elif select_query == "Tracking Cancelled Deliveries":
    cursor.execute(sql_queries[16])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[16], connection)
    st.dataframe(df)
elif select_query == "Frequent Vehicle Used for Delivery":
    cursor.execute(sql_queries[17])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[17], connection)
    st.dataframe(df)
elif select_query == "Average Delivery Time":
    cursor.execute(sql_queries[18])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[18], connection)
    st.dataframe(df)
elif select_query == "Average Delivery fee":
    cursor.execute(sql_queries[19])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[19], connection)
    st.dataframe(df)
elif select_query == "Average Distance Covered":
    cursor.execute(sql_queries[20])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[20], connection)
    st.dataframe(df)