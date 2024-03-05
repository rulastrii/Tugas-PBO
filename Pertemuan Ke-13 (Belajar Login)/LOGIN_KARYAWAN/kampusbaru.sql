-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 21 Jan 2024 pada 08.56
-- Versi Server: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `kampusbaru`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `mahasiswa`
--

CREATE TABLE IF NOT EXISTS `mahasiswa` (
`id` int(11) NOT NULL,
  `nim` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` enum('L','P') NOT NULL,
  `kode_prodi` enum('TIF','IND','PET') NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `jk`, `kode_prodi`) VALUES
(1, 1001, 'Rafli Hamzah', 'L', 'TIF'),
(2, 1002, 'Toni', 'L', 'IND'),
(3, 1003, 'Enni', 'P', 'TIF'),
(4, 1004, 'Lastri', 'P', 'PET');

-- --------------------------------------------------------

--
-- Struktur dari tabel `matakuliah`
--

CREATE TABLE IF NOT EXISTS `matakuliah` (
`id` int(11) NOT NULL,
  `kodemk` varchar(10) NOT NULL,
  `namamk` varchar(255) NOT NULL,
  `sks` enum('1','2','3','4') NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `matakuliah`
--

INSERT INTO `matakuliah` (`id`, `kodemk`, `namamk`, `sks`) VALUES
(1, '1001', 'Java 1', '4'),
(2, '1004', 'Basis Data', '2'),
(3, '2044', 'Pemrograman Web', '3'),
(20, '2045', 'Matematika', '2');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','dosen','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `email`, `nama`, `password`, `level`) VALUES
(1, 'nurjati@umc.ac.id', 'Nurjati', '$2y$10$BzqqNPejAUyOraPKKKCK2.xbrToZgOq9GnlmBtAMThvtB2zCTg4O.', 'mahasiswa'),
(2, 'rahman@gmail.com', 'Rahman', '$2y$10$NgiUETWu9BYXGKOTil.aOO5NobC1Nq5kREKYxG9cdnl4rhUZ/Tpci', 'dosen'),
(3, 'fitri@gmail.com', 'dr. Fitri', '$2y$10$i.GRsHyXlF0DUlIyGF96Zul5PFkm3Rq7C/1WOxd19WmKQercK5J8i', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `nim` (`nim`);

--
-- Indexes for table `matakuliah`
--
ALTER TABLE `matakuliah`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodemk` (`kodemk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `matakuliah`
--
ALTER TABLE `matakuliah`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
