import { useHistory } from "react-router";

const HomePage = () => {
  const history = useHistory();
  return (
    <div className="not-found-page">
      <div className="text-center">
        <p className="text-5xl font-bold secondary-font secondary mb-4">
          Home Page
        </p>
      </div>
    </div>
  );
};

export default HomePage;
