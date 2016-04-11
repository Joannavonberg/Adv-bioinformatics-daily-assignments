SELECT C.CategoryName
FROM Categories C
JOIN Products P ON C.CategoryID = P.CategoryID
JOIN OrderDetails OD ON P.ProductID = OD.ProductID
JOIN Orders O ON OD.OrderID = O.OrderID
WHERE O.OrderDate > 1996-12-10
