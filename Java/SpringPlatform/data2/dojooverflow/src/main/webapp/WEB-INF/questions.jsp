<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Questions</title>
</head>
<body>
<h1>Questions Dashboard</h1>
<table>
    <thead>
        <tr>
            <th>BLAH</th>
            <th>BLAH</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach var="item" items="${list_of_items}">
            <tr>
                <td>${item.question}</td>
                <td>
                	<c:forEach var="tag" items="${item.tags}">${tag.subject},</c:forEach>
                </td>
            </tr>
        </c:forEach>
    </tbody>
</table>
<a href="/questions/new">New Question</a>
</body>
</html>