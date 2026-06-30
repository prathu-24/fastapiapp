import { useEffect, useState } from "react";
import Welcome from "./components/Welcome";
import NavBar from "./components/NavBar";
import CompanyCard from "./components/CompanyCard";
import Footer from "./components/Footer";
import { getCompanies } from "./Services/CompanyServices";
import type { Company } from "./types/company";

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [companies, setCompanies] = useState<Company[]>([]);

  async function fetchCompanies() {
    setLoading(true);

    try {
      const companiesData = await getCompanies();
      setCompanies(companiesData);
    } catch (error) {
      setError(error as Error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchCompanies();
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>{error.message}</h2>;
  }

  return (
    <>
      <NavBar />
      <Welcome />

      {companies.map((company) => (
        <CompanyCard key={company.id} company={company} />
      ))}

      <Footer />
    </>
  );
}

export default App;