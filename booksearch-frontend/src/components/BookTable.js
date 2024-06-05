import React, { useState, useEffect } from 'react';
import { IconButton, Table, TableBody, TableCell, TableHead, TableRow, Typography, Box, Paper } from '@mui/material';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';

function BookTable({ books, onLike, recommendations }) {
    const [likedBooks, setLikedBooks] = useState(() => {
        const saved = localStorage.getItem('likedBooks');
        return saved ? JSON.parse(saved) : [];
    });

    useEffect(() => {
        localStorage.setItem('likedBooks', JSON.stringify(likedBooks));
        onLike(likedBooks);
    }, [likedBooks, onLike]);

    const likeBook = (bookId) => {
        setLikedBooks(prevLikedBooks => {
            if (prevLikedBooks.includes(bookId)) {
                return prevLikedBooks.filter(id => id !== bookId);
            } else {
                return [...prevLikedBooks, bookId];
            }
        });
    };

    return (
        <div>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Title</TableCell>
                        <TableCell>Author</TableCell>
                        <TableCell>Price</TableCell>
                        <TableCell>Genre</TableCell>
                        <TableCell>Summary</TableCell>
                        <TableCell>Like</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {books.map(book => (
                        <TableRow key={book.id}>
                            <TableCell>{book.title}</TableCell>
                            <TableCell>{book.author}</TableCell>
                            <TableCell>{book.price}</TableCell>
                            <TableCell>{book.genre}</TableCell>
                            <TableCell>{book.summary}</TableCell>
                            <TableCell>
                                <IconButton
                                    onClick={() => likeBook(book.id)}
                                    color={likedBooks.includes(book.id) ? 'primary' : 'default'}
                                >
                                    <ThumbUpIcon />
                                </IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>

            {recommendations.length > 0 && (
                <Box sx={{ padding: '16px' }}>
                    <Paper elevation={3} sx={{ padding: '16px' }}>
                        <Typography variant="h6">Recommended Books</Typography>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <TableCell>Title</TableCell>
                                    <TableCell>Author</TableCell>
                                    <TableCell>Price</TableCell>
                                    <TableCell>Genre</TableCell>
                                    <TableCell>Summary</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {recommendations.map(book => (
                                    <TableRow key={book.id}>
                                        <TableCell>{book.title}</TableCell>
                                        <TableCell>{book.author}</TableCell>
                                        <TableCell>{book.price}</TableCell>
                                        <TableCell>{book.genre}</TableCell>
                                        <TableCell>{book.summary}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </Paper>
                </Box>
            )}
        </div>
    );
}

export default BookTable;
