-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2024 at 04:36 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parkiran`
--

-- --------------------------------------------------------

--
-- Table structure for table `lapor`
--

CREATE TABLE `lapor` (
  `id` int(11) NOT NULL,
  `nopolhilang` varchar(10) NOT NULL,
  `keterangan` varchar(100) NOT NULL,
  `tanggal` date NOT NULL,
  `jamlapor` time NOT NULL,
  `jenis` enum('Motor','Mobil') NOT NULL DEFAULT 'Motor',
  `bukti` enum('STNK','BPKB','Faktur','Surat Beli') DEFAULT 'STNK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lapor`
--

INSERT INTO `lapor` (`id`, `nopolhilang`, `keterangan`, `tanggal`, `jamlapor`, `jenis`, `bukti`) VALUES
(45, 'E 1918 TT', 'Honda Civic Merah', '2024-02-19', '21:15:37', 'Mobil', 'STNK'),
(46, 'E 7889 YY', 'Yamaha Mio', '2024-02-19', '21:39:22', 'Motor', 'BPKB');

-- --------------------------------------------------------

--
-- Table structure for table `parkir`
--

CREATE TABLE `parkir` (
  `id` int(11) NOT NULL,
  `nopol` varchar(10) NOT NULL,
  `tanggal` date NOT NULL,
  `jenis` enum('Motor','Mobil') NOT NULL DEFAULT 'Motor',
  `masuk` time NOT NULL,
  `keluar` time NOT NULL,
  `tarif` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parkir`
--

INSERT INTO `parkir` (`id`, `nopol`, `tanggal`, `jenis`, `masuk`, `keluar`, `tarif`) VALUES
(36, 'E 1918 TT', '2024-02-16', 'Mobil', '07:55:24', '09:17:41', '5485.555555555556'),
(37, 'E 7889 YY', '2024-02-19', 'Motor', '08:50:27', '09:00:27', '333.3333333333333'),
(38, 'E 1234 UI', '2024-02-19', 'Mobil', '09:08:19', '09:08:19', '0.0'),
(39, 'D 2345 JK', '2024-02-19', 'Mobil', '08:50:27', '08:50:27', '0.0'),
(40, 'B 2389 IL', '2024-02-19', 'Motor', '08:50:27', '08:50:27', '0.0'),
(41, 'E 1967 GH', '2024-02-19', 'Mobil', '08:50:27', '08:50:27', '0.0'),
(42, 'F 1255 TY', '2024-02-19', 'Motor', '08:50:27', '08:50:27', '0.0'),
(43, 'T 7688 OIK', '2024-02-19', 'Mobil', '08:50:27', '08:50:27', '0.0'),
(44, 'E 2345 KL', '2024-02-19', 'Mobil', '08:50:27', '08:50:27', '0.0'),
(46, 'T 7890 GH', '2024-02-19', 'Mobil', '08:50:27', '08:50:27', '0.0'),
(47, 'E 7766 KL', '2024-02-19', 'Motor', '09:37:26', '09:37:26', '0.0');

-- --------------------------------------------------------

--
-- Table structure for table `upah`
--

CREATE TABLE `upah` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `username` varchar(100) NOT NULL,
  `rolename` enum('petugas','manajer','direktur') NOT NULL DEFAULT 'direktur',
  `status` enum('Tetap','Tidak Tetap') NOT NULL DEFAULT 'Tetap',
  `gaji` enum('Rp 500.000','Rp 1.500.000','Rp 2.500.000','Rp 3.000.000') DEFAULT 'Rp 500.000'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `upah`
--

INSERT INTO `upah` (`id`, `nama`, `username`, `rolename`, `status`, `gaji`) VALUES
(20, 'Rulastri', 'lastri06@gmail.com', 'petugas', 'Tetap', 'Rp 1.500.000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `iduser` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rolename` enum('petugas','manajer','direktur') NOT NULL DEFAULT 'petugas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`iduser`, `username`, `password`, `rolename`) VALUES
(1, 'lastri06@gmail.com', '202cb962ac59075b964b07152d234b70', 'petugas'),
(2, 'manajer@gmail.com', '202cb962ac59075b964b07152d234b70', 'manajer'),
(3, 'direktur@gmail.com', '202cb962ac59075b964b07152d234b70', 'direktur');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lapor`
--
ALTER TABLE `lapor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nopolhilang` (`nopolhilang`),
  ADD KEY `jenis` (`jenis`);

--
-- Indexes for table `parkir`
--
ALTER TABLE `parkir`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nopol` (`nopol`),
  ADD KEY `jenis` (`jenis`);

--
-- Indexes for table `upah`
--
ALTER TABLE `upah`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `nama` (`nama`),
  ADD KEY `rolename` (`rolename`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`iduser`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `rolename` (`rolename`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lapor`
--
ALTER TABLE `lapor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `parkir`
--
ALTER TABLE `parkir`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `upah`
--
ALTER TABLE `upah`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `iduser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `lapor`
--
ALTER TABLE `lapor`
  ADD CONSTRAINT `lapor_ibfk_1` FOREIGN KEY (`nopolhilang`) REFERENCES `parkir` (`nopol`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `lapor_ibfk_2` FOREIGN KEY (`jenis`) REFERENCES `parkir` (`jenis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `upah`
--
ALTER TABLE `upah`
  ADD CONSTRAINT `upah_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `upah_ibfk_2` FOREIGN KEY (`rolename`) REFERENCES `users` (`rolename`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
