import React from 'react';

const Navbar = () => {
    return (
        <div className="navbar">
            <div className="main-nav">
                <div className="nav-item">
                    <div className="nav-logo">
                        <h1>LOGO</h1>
                    </div>
                </div>
                <div className="nav-item">
                    <div className="nav-searchbar">
                        <div className="categories">
                            <span>Catégories</span>
                            <i className="fa fa-sort-down" />
                        </div>
                        <input placeholder="Rechercher..." />
                        <div className="icon">
                            <i className="fa fa-search" />
                        </div>
                    </div>
                </div>
                <div className="nav-item">
                    <div className="nav-icon-text login">
                        <div className="icon">
                            <i className="fa fa-user-circle" />
                        </div>
                        <div className="text">Mon compte</div>
                    </div>
                </div>
                <div className="nav-item">
                    <div className="nav-icon-text basket">
                        <div className="icon">
                            <i className="fa fa-shopping-cart" />
                        </div>
                        <div className="text">Mon panier</div>
                    </div>
                </div>
            </div>

            <div className="sub-nav">
                <div className="nav-item"></div>
            </div>
        </div>

    );
};

export default Navbar;
