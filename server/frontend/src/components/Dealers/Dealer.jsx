import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png";
import neutral_icon from "../assets/neutral.png";
import negative_icon from "../assets/negative.png";
import review_icon from "../assets/reviewbutton.png";
import Header from '../Header/Header';

const Dealer = () => {
  const [dealer, setDealer] = useState({});
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [postReview, setPostReview] = useState(<></>);

  let curr_url = window.location.href;
  let root_url = curr_url.includes("dealer") ? curr_url.substring(0, curr_url.indexOf("dealer")) : "/";
  let params = useParams();
  let id = params.id;

  // URLs pour les appels API
  let dealer_url = root_url + `djangoapp/dealer/${id}`;
  let reviews_url = root_url + `djangoapp/reviews/dealer/${id}`;
  let post_review = root_url + `djangoapp/add_review`; // Correction de l'URL

  // Fonction pour récupérer les détails du concessionnaire
  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url, { method: "GET" });
      if (!res.ok) throw new Error("Failed to fetch dealer data");
      const retobj = await res.json();

      if (retobj.status === 200 && Array.isArray(retobj.dealer) && retobj.dealer.length > 0) {
        setDealer(retobj.dealer[0]);
      }
    } catch (error) {
      console.error("Error fetching dealer:", error);
    }
  };

  // Fonction pour récupérer les avis
  const get_reviews = async () => {
    try {
      const res = await fetch(reviews_url, { method: "GET" });
      if (!res.ok) throw new Error("Failed to fetch reviews");
      const retobj = await res.json();

      if (retobj.status === 200) {
        if (Array.isArray(retobj.reviews) && retobj.reviews.length > 0) {
          setReviews(retobj.reviews);
        } else {
          setUnreviewed(true);
        }
      }
    } catch (error) {
      console.error("Error fetching reviews:", error);
    }
  };

  // Fonction pour obtenir l'icône de sentiment
  const senti_icon = (sentiment) => {
    return sentiment === "positive"
      ? positive_icon
      : sentiment === "negative"
      ? negative_icon
      : neutral_icon;
  };

  // Effet pour charger les données au montage
  useEffect(() => {
    get_dealer();
    get_reviews();

    if (sessionStorage.getItem("username")) {
      setPostReview(
        <a href={post_review}>
          <img
            src={review_icon}
            style={{ width: "10%", marginLeft: "10px", marginTop: "10px" }}
            alt="Post Review"
          />
        </a>
      );
    }
  }, []);

  return (
    <div style={{ margin: "20px" }}>
      <Header />
      <div style={{ marginTop: "10px" }}>
        {/* Affichage conditionnel pour le nom du concessionnaire */}
        <h1 style={{ color: "grey" }}>
          {dealer?.full_name || "Sample"} {postReview}
        </h1>
        <h4 style={{ color: "grey" }}>
          {dealer?.city && `${dealer.city},`}
          {dealer?.address && `${dealer.address},`}
          {dealer?.zip && ` Zip - ${dealer.zip},`}
          {dealer?.state && dealer.state}
        </h4>
      </div>
      {/* Affichage des avis */}
      <div className="reviews_panel">
        {reviews.length === 0 && unreviewed === false ? (
          <text>Loading Reviews....</text>
        ) : unreviewed === true ? (
          <div>No reviews yet!</div>
        ) : (
          reviews.map((review, index) => (
            <div className="review_panel" key={index}>
              <img src={senti_icon(review.sentiment)} className="emotion_icon" alt="Sentiment" />
              <div className="review">{review.review}</div>
              <div className="reviewer">
                {review.name} {review.car_make} {review.car_model} {review.car_year}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Dealer;