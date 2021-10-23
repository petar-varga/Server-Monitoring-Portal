import { Button } from "antd";
import { useHistory } from "react-router";

import { INDEX_ROUTE } from "../../routes";

const NotFoundPage = () => {
  const history = useHistory();
  return (
    <div className="not-found-page">
      <div className="text-center">
        <p className="text-5xl font-bold secondary-font secondary mb-4">
          Error 404
        </p>
        <p className="text-2xl secondary">
          What you were looking for could not be found.
        </p>
        <Button
          size="large"
          type="primary"
          className="mt-20"
          onClick={() => history.push(INDEX_ROUTE)}
        >
          Go back to home
        </Button>
      </div>
    </div>
  );
};

export default NotFoundPage;
