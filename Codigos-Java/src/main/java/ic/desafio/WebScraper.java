package ic.desafio;

import net.lingala.zip4j.ZipFile;
import java.io.*;
import java.net.URL;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class WebScraper {
	// Caminhos relativos considerando sua estrutura
	private static final String ANEXOS_DIR = "../Anexos";
	private static final String ZIP_FILE = ANEXOS_DIR + "/Anexos_Compactados.zip";

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		try {
			// Verificar/Criar diretório
			Path anexosPath = Paths.get(ANEXOS_DIR);
			if (!Files.exists(anexosPath)) {
				Files.createDirectories(anexosPath);
			}

			// Solicitar URLs
			System.out.print("URL completa do Anexo I (PDF): ");
			String url1 = scanner.nextLine().trim();

			System.out.print("URL completa do Anexo II (PDF): ");
			String url2 = scanner.nextLine().trim();

			// Lista para controle dos downloads
			List<String> downloadedFiles = new ArrayList<>();

			// Download Anexo I
			String fileName1 = "Anexo_I.pdf";
			downloadFile(url1, ANEXOS_DIR + "/" + fileName1);
			downloadedFiles.add(ANEXOS_DIR + "/" + fileName1);

			// Download Anexo II
			String fileName2 = "Anexo_II.pdf";
			downloadFile(url2, ANEXOS_DIR + "/" + fileName2);
			downloadedFiles.add(ANEXOS_DIR + "/" + fileName2);

			// Compactação
			createZip(downloadedFiles);
			System.out.println("\nProcesso concluído com sucesso!");
			System.out.println("Arquivo ZIP criado em: " + new File(ZIP_FILE).getAbsolutePath());

		} catch (Exception e) {
			System.err.println("Erro: " + e.getMessage());
			e.printStackTrace();
		} finally {
			scanner.close();
		}
	}

	private static void downloadFile(String fileUrl, String destination) throws IOException {
		System.out.println("Baixando: " + fileUrl);
		try (InputStream in = new URL(fileUrl).openStream()) {
			Files.copy(in, Paths.get(destination), StandardCopyOption.REPLACE_EXISTING);
		}
		System.out.println("Salvo em: " + destination);
	}

	private static void createZip(List<String> files) throws IOException {
		System.out.println("\nCriando arquivo ZIP...");
		ZipFile zipFile = new ZipFile(ZIP_FILE);
		for (String file : files) {
			zipFile.addFile(new File(file));
		}

		// Opcional: Remover PDFs após compactar
		for (String file : files) {
			Files.deleteIfExists(Paths.get(file));
		}
	}
}