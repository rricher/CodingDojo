<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Dashboard</title>
</head>
<body>
	<a href="/cart">Cart (${cartsize})</a>
	<table>
    <thead>
        <tr>
            <th>name</th>
            <th>price</th>
            <th>image</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach var="item" items="${products}">
            <tr>
                <td><a href="/product/${item.id}">${item.name}</a></td>
                <td>${item.price}</td>
                <td><img src="${item.img}" alt="${item.name}"></td>
            </tr>
        </c:forEach>
    </tbody>
</table>
</body>
</html>