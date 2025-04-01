package ic.desafio;

import net.lingala.zip4j.ZipFile;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import java.io.*;
import java.net.URL;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class WebScraper {
	private static final String ANEXOS_DIR = "../Outros_Arquivos/Anexos";
	private static final String ZIP_FILE = ANEXOS_DIR + "/Anexos_Compactados.zip";
	private static final String ANS_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos";

	public static void main(String[] args) {
		try {
			// Cria o diretório automaticamente caso ele não exista
			Files.createDirectories(Paths.get(ANEXOS_DIR));

			System.out.println("Acessando o site da ANS...");
			Document doc = Jsoup.connect(ANS_URL).get();

			// Procura os links dos anexos
			List<Element> pdfLinks = new ArrayList<>();
			for (Element link : doc.select("a[href$=.pdf]")) {
				String linkText = link.text();
				String href = link.attr("href").toLowerCase();

				if (linkText.contains("Anexo") || href.contains("anexo")) {
					pdfLinks.add(link);
				}
			}

			if (pdfLinks.isEmpty()) {
				throw new IOException("Nenhum link de Anexo encontrado na página!");
			}

			List<String> downloadedFiles = new ArrayList<>();

			for (Element link : pdfLinks) {
				String pdfUrl = link.attr("abs:href");
				String fileName = pdfUrl.substring(pdfUrl.lastIndexOf('/') + 1);
				String destination = ANEXOS_DIR + "/" + fileName;

				downloadFile(pdfUrl, destination);
				downloadedFiles.add(destination);
				System.out.println("Encontrado: " + link.text() + " -> " + fileName);
			}

			// Compacta os arquivos
			createZip(downloadedFiles);
			System.out.println("\n✅ Concluído! ZIP criado em: " + new File(ZIP_FILE).getAbsolutePath());

		} catch (Exception e) {
			System.err.println("❌ Erro: " + e.getMessage());
			e.printStackTrace();
		}
	}

	private static void downloadFile(String fileUrl, String destination) throws IOException {
		System.out.println("\nBaixando: " + fileUrl);
		try (InputStream in = new URL(fileUrl).openStream()) {
			long bytes = Files.copy(in, Paths.get(destination), StandardCopyOption.REPLACE_EXISTING);
			System.out.println("✔️ Salvo (" + bytes / 1024 + " KB): " + destination);
		}
	}

	private static void createZip(List<String> files) throws IOException {
		System.out.println("\nCompactando...");
		ZipFile zipFile = new ZipFile(ZIP_FILE);
		for (String file : files) {
			zipFile.addFile(new File(file));
			Files.deleteIfExists(Paths.get(file));
		}
	}
}