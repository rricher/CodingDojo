<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>   
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h1>This is Dojos and Ninjas</h1>
	<table>
    <thead>
        <tr>
            <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach var="item" items="${myDojos}">
            <tr>
                <td>${item.name}</td>
            </tr>
        </c:forEach>
    </tbody>
</table>
<table>
    <thead>
        <tr>
            <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach var="item" items="${myNinjas}">
            <tr>
                <td>${item.firstName}</td>
            </tr>
        </c:forEach>
    </tbody>
</table>
</body>
</html>