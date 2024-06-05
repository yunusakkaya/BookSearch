import React, { useState } from 'react';
import { Box, TextField, IconButton, Grid, Paper } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

function SearchBar({ onSearch }) {
    const [input, setInput] = useState('');
    const [author, setAuthor] = useState('');
    const [minPrice, setMinPrice] = useState('');
    const [maxPrice, setMaxPrice] = useState('');
    const [genre, setGenre] = useState('');

    const handleInputChange = (event) => {
        setInput(event.target.value);
    };

    const handleAuthorChange = (event) => {
        setAuthor(event.target.value);
    };

    const handleMinPriceChange = (event) => {
        setMinPrice(event.target.value);
    };

    const handleMaxPriceChange = (event) => {
        setMaxPrice(event.target.value);
    };

    const handleGenreChange = (event) => {
        setGenre(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        onSearch({ query: input, author, minPrice, maxPrice, genre });
    };

    return (
        <Paper elevation={3} sx={{ padding: '16px', margin: '16px' }}>
            <Box
                component="form"
                onSubmit={handleSubmit}
                sx={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexDirection: 'column',
                }}
            >
                <Grid container spacing={2} alignItems="center" justifyContent="center">
                    <Grid item xs={12} sm={6}>
                        <TextField
                            label="Search Books"
                            variant="outlined"
                            value={input}
                            onChange={handleInputChange}
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <TextField
                            label="Author"
                            variant="outlined"
                            value={author}
                            onChange={handleAuthorChange}
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={6} sm={3}>
                        <TextField
                            label="Min Price"
                            variant="outlined"
                            value={minPrice}
                            onChange={handleMinPriceChange}
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={6} sm={3}>
                        <TextField
                            label="Max Price"
                            variant="outlined"
                            value={maxPrice}
                            onChange={handleMaxPriceChange}
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <TextField
                            label="Genre"
                            variant="outlined"
                            value={genre}
                            onChange={handleGenreChange}
                            fullWidth
                        />
                    </Grid>
                    <Grid item>
                        <IconButton type="submit" color="primary" aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Grid>
                </Grid>
            </Box>
        </Paper>
    );
}

export default SearchBar;
