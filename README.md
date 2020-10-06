# Northwind_redo

The goal of this project will be to conduct business analysis for Northwind Traders, a ficticious company.

There are a number of business questions that will be assessed:
- Does discount amount have an impact on quantity of goods sold in an order?

This cleaner version will attempt to optimize the SQL queries - while I utilized Python to join data frames in the first round of analysis, I will use sqlite to manipulate the data first, reducing the code to be run following the queries.

I also explore the possible gross profit margins seen across product categories and breakout the needed increase in quantity sold to match a discount provided given a possible existing profit margin. I estimate that Northwinds will have a gpm between 30-50% on goods sold, however, accessing real COGS would help better target that figure.

## The Data
The data for this project is pulled from a publicly available sqlite database for Northwind Traders. There are a number of tables in the database, and they can be seen here:

![alt text](https://github.com/zachzazueta/Northwinds_redo/blob/master/Northwind.png)

As you can see, there is information about orders, customers, employees, and business related matters (shippers, etc). This is an entirely plausible example of a company's relational database, as it stores key information about business structure and function. Parts that would be nice to see would be tables providing information about the expense side of Northwinds, as this would strengthen business analysis.

## Libraries and queries

Standard libraries - pandas, numpy, seaborn - were used in data cleaning and light visualizations for this project. I also employed the use of sqlite3 to generate SQL queries directly in my Notebooks. I utilize statsmodels and scipy for T Tests, Least Squares regression, and Chi Squared tests.

I also wrote a few functions in a separate file, ProjectFunctions, and import them, showcasing the use of a separate file storage for functions which might be used again in future work.

```
conn = sqlite3.Connection('Northwind_small.sqlite')

od_query = pd.read_sql('''SELECT a.OrderId, a.ProductId, a.UnitPrice, a.Quantity, a.Discount, c.CategoryName 
                          FROM OrderDetail a LEFT JOIN Product b ON a.ProductId = b.ID LEFT JOIN Category c ON b.CategoryId = c.ID
                          WHERE (a.Discount != 0.01 AND a.Discount != 0.02 AND a.Discount != 0.03 AND a.Discount != 0.04 
                          AND a.Discount != 0.06)''', conn)

df = pd.DataFrame(od_query)
```

See an example of the workbook below:

![alt text](https://github.com/zachzazueta/Northwinds_redo/blob/master/tableau.PNG)
