import type { Company } from "../types/company";

interface CompanyCardProps {
  company: Company;
}

function CompanyCard({ company }: CompanyCardProps) {
  return (
    <div
      style={{
        border: "1px solid gray",
        margin: "10px",
        padding: "10px",
        borderRadius: "8px",
      }}
    >
      <h2>{company.name}</h2>

      <p>
        <strong>Email:</strong> {company.email}
      </p>

      <p>
        <strong>Phone:</strong> {company.phone}
      </p>

      <p>
        <strong>Location:</strong> {company.location}
      </p>
    </div>
  );
}

export default CompanyCard;