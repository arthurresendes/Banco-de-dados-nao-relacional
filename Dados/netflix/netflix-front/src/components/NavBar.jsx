import React from 'react'
import { Link } from 'react-router-dom'
import { useLocation } from 'react-router-dom'

const NavBar = () => {
    const location = useLocation()

    const links = [
        { to: '/', label: 'Top 5 Netflix' },
        { to: '/seculo-1900', label: 'Filmes Anos 1900' },
        { to: '/find-name', label: 'Busca por nome' },
        { to: '/find-actor', label: 'Busca por nome' },
    ]

    return (
        <nav>
            {links.map(({ to, label }) => (
                <Link
                    key={to}
                    to={to}
                    style={{ marginRight: '1rem', fontWeight: location.pathname === to ? 'bold' : 'normal' }}
                >
                    {label}
                </Link>
            ))}
        </nav>
    )
}

export default NavBar