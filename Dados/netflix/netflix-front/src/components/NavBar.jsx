import { Link, useLocation } from 'react-router-dom'

const NavBar = () => {
    const location = useLocation()

    const links = [
        { to: '/', label: 'Top 5 filmes/séries por tipo' },
        { to: '/seculo-1900', label: 'Filmes Anos 1900' },
        { to: '/find-name', label: 'Busca por nome' },
        { to: '/find-actor', label: 'Busca por ator' },
        { to: '/register', label: 'Cadastrar filme/série' },
        { to: '/update-cast', label: 'Atualizar Cast' },
        { to: '/delete-movie', label: 'Deletar por nome' },
    ]

    return (
        <nav className="navbar">
            {links.map(({ to, label }) => (
                <Link
                    key={to}
                    to={to}
                    className={location.pathname === to ? "active" : ""}
                >
                    {label}
                </Link>
            ))}
        </nav>
    )
}

export default NavBar