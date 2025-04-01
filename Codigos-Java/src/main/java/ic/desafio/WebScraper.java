package ic.desafio;

import net.lingala.zip4j.ZipFile;
import java.io.*;
import java.net.URL;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class WebScraper {
	private static final String ANEXOS_DIR = "../Outros_Arquivos/Anexos";
	private static final String ZIP_FILE = ANEXOS_DIR + "/Anexos_Compactados.zip";

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		try {
			// Cria o diretório automaticamente caso ele não exista
			Path anexosPath = Paths.get(ANEXOS_DIR);
			if (!Files.exists(anexosPath)) {
				Files.createDirectories(anexosPath);
			}

			// Solicita os links dos Anexos
			System.out.print("Insira a URL completa do Anexo_I.pdf: ");
			String url1 = scanner.nextLine().trim();
			System.out.print("Insira a URL completa do Anexo_II.pdf: ");
			String url2 = scanner.nextLine().trim();

			List<String> downloadedFiles = new ArrayList<>();

			// Download dos Anexos 1 e 2
			String fileName1 = "Anexo_I.pdf";
			downloadFile(url1, ANEXOS_DIR + "/" + fileName1);
			downloadedFiles.add(ANEXOS_DIR + "/" + fileName1);
			String fileName2 = "Anexo_II.pdf";
			downloadFile(url2, ANEXOS_DIR + "/" + fileName2);
			downloadedFiles.add(ANEXOS_DIR + "/" + fileName2);

			// Compactação dos Anexos baixados
			createZip(downloadedFiles);
			System.out.println("\nProcesso concluído com sucesso!");
			System.out.println("Arquivo ZIP criado em: " + new File(ZIP_FILE).getAbsolutePath());

		} catch (Exception e) {
			System.err.println(e.getMessage());
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

		// Exclui os Anexos após compactar
		for (String file : files) {
			Files.deleteIfExists(Paths.get(file));
		}
	}
}