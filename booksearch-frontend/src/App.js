import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import BookTable from './components/BookTable';
import { AppBar, Toolbar, Typography, Button, Box, Paper } from '@mui/material';

function App() {
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [likedBooks, setLikedBooks] = useState(() => {
        const saved = localStorage.getItem('likedBooks');
        return saved ? JSON.parse(saved) : [];
    });
    const [recommendedBooks, setRecommendedBooks] = useState([]);

    const searchBooks = async ({ query, author, minPrice, maxPrice, genre }) => {
        setLoading(true);
        setError('');
        try {
            const response = await axios.get('http://127.0.0.1:8000/search/', {
                params: {
                    q: query,
                    author,
                    min_price: minPrice,
                    max_price: maxPrice,
                    genre
                }
            });
            setBooks(response.data);
        } catch (error) {
            console.error('Error fetching books:', error);
            setError('Failed to fetch books.');
        } finally {
            setLoading(false);
        }
    };

    const updateLikedBooks = (likedBooks) => {
        setLikedBooks(likedBooks);
        getRecommendations(likedBooks);
    };

    const getRecommendations = async (likedBooks) => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/recommendations/', {
                book_ids: likedBooks
            });
            setRecommendedBooks(response.data);
        } catch (error) {
            console.error('Error fetching recommendations:', error);
        }
    };

    useEffect(() => {
        const savedLikedBooks = JSON.parse(localStorage.getItem('likedBooks')) || [];
        if (savedLikedBooks.length > 0) {
            getRecommendations(savedLikedBooks);
        }
    }, []);

    return (
        <div className="App">
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" style={{ flexGrow: 1 }}>
                        BookSearch
                    </Typography>
                </Toolbar>
            </AppBar>
            <header className="App-header">
                <h1>BookSearch</h1>
                <SearchBar onSearch={searchBooks} />
                {loading && <p>Loading...</p>}
                {error && <p className="error">{error}</p>}
                {!loading && !error && books.length > 0 && (
                    <BookTable books={books} onLike={updateLikedBooks} recommendations={recommendedBooks} />
                )}
                {!loading && !error && books.length === 0 && <p>No books found.</p>}
            </header>
        </div>
    );
}

export default App;
