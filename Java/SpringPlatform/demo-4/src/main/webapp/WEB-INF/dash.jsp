<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>    
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Registration Page</title>
</head>
<body>
      <table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Network</th>
            <th>Average</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach var="item" items="${shows}">
            <tr>
                <td>
                	<a href="/show/${item.id}">${item.title}</a>
                </td>
                <td>${item.network}</td>
                <td>${item.average }</td>
                <c:if test="${item.creator.id == userid }">
                <td>
                    <a href="/edit/${item.id}">Edit</a> |
                    <a href="/delete/${item.id}">Delete</a>
                </td>
                </c:if>
            </tr>
        </c:forEach>
    </tbody>
</table>
</body>
</html>