<template>
  <div class="container">
    <div class="header">Текущее время:</div>
    <div class="clock">{{ hours }}:{{ minutes }}</div>
    <div class="cards">
      <img
        :src="u"
        v-for="(u, i) in getCardsUrls()"
        class="card"
        :key="u"
        :id="'image_' + i"
      />
    </div>
    <div>
      {{ currentCards[0]["flavor"] }} <br/>
      {{ currentCards[1]["flavor"] }}
    </div>
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log", "error"] }] */
// import Sunwell from 'sunwell';
// let sw = new Sunwell();
import cards from "@/assets/parsed_new.js";
const imageURL =
  "https://art.hearthstonejson.com/v1/render/latest/ruRU/512x/<ID>.png";
export default {
  name: "MainView",
  data: function () {
    return {
      cards: cards,
      currentCards: [],
      range: [],
    };
  },
  created: function () {
    this.currentCards = this.getCardByTime(this.time);
    setInterval(() => {
      this.currentCards = this.getCardByTime(this.time);
      this.$forceUpdate();
    }, 1000 * 30);
  },
  methods: {
    getCardsUrls() {
      let cards = this.currentCards;
      let ans = [];
      for (let i = 0; i < cards.length; i++) {
        ans.push(imageURL.replace("<ID>", cards[i].id));
      }
      return ans;
    },
    getCardByTime: function (time) {
      let mill = [
        {
          artist: "Jim Nelson",
          attack: 4,
          cardClass: "NEUTRAL",
          collectible: true,
          cost: 2,
          dbfId: 855,
          elite: true,
          flavor: "«Давай зажигать, крошка!»",
          health: 4,
          id: "NEW1_029",
          mechanics: ["BATTLECRY"],
          name: "Миллхаус Манашторм",
          rarity: "LEGENDARY",
          set: "EXPERT1",
          text:
            "<b>Боевой клич:</b> в следующий ход противника его заклинания стоят (0).",
          type: "MINION",
        },
      ];
      let card1 = this.cards[Math.floor(time / 60).toString()] || mill;
      let card2 = this.cards[(time % 60).toString()] || mill;
      function choose(choices) {
        var index = Math.floor(Math.random() * choices.length);
        return choices[index];
      }
      card1 = choose(card1);
      card2 = choose(card2);
      return [card1, card2];
    },
  },
  computed: {
    minutes: function () {
      return new Date().getMinutes();
    },
    hours: function () {
      return new Date().getHours() % 12;
    },
    time: function () {
      return (new Date().getHours() % 12) * 60 + new Date().getMinutes();
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: center;
  margin: 0 auto;
}

.header {
  font-size: 30px;
}

.clock {
  font-size: 40px;
  font-weight: bold;
}

.cards {
  /* position: absolute; */
  display: flex;
  width: 100%;
  text-align: center;
  align-items: center;
  justify-content: center;
}

.card {
  display: block;
  /* margin-left: auto;
  margin-right: auto; */
  width: 200px;

  margin-top: -10px;
}
</style>
