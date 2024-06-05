import React from 'react';

function BookList({ books }) {
    return (
        <ul>
            {books.map(book => (
                <li key={book.id}>{book.title} - {book.author}</li>
            ))}
        </ul>
    );
}

export default BookList;
