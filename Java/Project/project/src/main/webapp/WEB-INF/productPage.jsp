<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>   
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>This is a Product</title>
</head>
<body>
	<h1>${product.name}</h1>
	<img src="${product.img}" alt="${product.name}">
	<p>Price: ${product.price}</p>
	<p>Description: ${product.desc}</p>
	<p>Categories:</p>
	<ul>
		<c:forEach var="item" items="${product.categories}">
		<li>${item.name}</li>
		</c:forEach>
	</ul>
</body>
</html>