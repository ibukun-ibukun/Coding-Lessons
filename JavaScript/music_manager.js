const prompt = require("prompt-sync")();

let playlist = [
  { title: "Obinigwe", artist: "GUC", genre: "Gospel Worship" },
  { title: "I Denounce You", artist: "Sheena Taylor", genre: "Gospel Rap" },
  { title: "Eze Yoyo", artist: "SZA", genre: "Gospel praise" },
  { title: "Way Maker", artist: "Sinach", genre: "Gospel Worship" },
  { title: "Nara", artist: "Judikay", genre: "Gospel Worship" }
];

function showPlaylist() {
    if (playlist.length === 0) {
        console.log("Your Playlist is empty.")
    }
    else {
        console.log("Your Playlist:");
        for (const song of playlist) {
            console.log(`${playlist}. ${song.title} — ${song.artist} — ${song.genre}`);
        }
    }    
}

function addSong() {
    const title = prompt("Enter song title: ");
    const artist = prompt("Enter artist: ");
    const genre = prompt("Enter genre: ");

    let songExists = false;

    for (const song of playlist) {
        if (song.title.toLowerCase() === title.toLowerCase()) {
            songExists = true;
            break;
        }
    }

    if (songExists) {
        console.log(`"${title}" is already in the playlist. Song not added.`);
    } else {
        const newSong = { title: title, artist: artist, genre: genre };
        playlist.push(newSong);
        console.log(`"${title}" by ${artist} has been added to the playlist.`);
    }
}

function searchByArtist() {
    const artistSearch = prompt("Enter artist name to search: ");
    let found = false;

    console.log(`Songs by ${artistSearch}:`);

    for (const song of playlist) {
        if (song.artist.toLowerCase() === artistSearch.toLowerCase()) {
        console.log(`${song.title} — ${song.genre}`);
        found = true;
        }
    }

    if (!found) {
        console.log(`No songs found for ${artistSearch}.`);
    }

}

function removeSong() {
    const titleToRemove = prompt("Enter the title of the song to remove: ");
    let found = false

    for (const song of playlist){
        if (titleToRemove.toLowerCase() === song.title.toLowerCase){
            found = true
        }
    }
    if (found){
        const songToRemove = {title: title, artist: artist, genre: genre}
            console.log(`${title} removed!`)
            playlist.splice(songToRemove)
    }
    else {
      console.log("No Song Found")
    }

}

function showGenres() {
  let genres = [];

  for (const song of playlist) {
    if (!genres.includes(song.genre)) {
      genres.push(song.genre);
    }
  }

  console.log(`Genres: ${genres.join(", ")}`);
}

function showMenu() {
  let running = true;

  while (running) {
    console.log("Music Playlist Manager");
    console.log("1. Show Playlist");
    console.log("2. Add Song")
    console.log("3. Search by Artist")
    console.log("4. Remove Song")
    console.log("5. Show Genres")
    console.log("6. Quit")
    const choice = prompt("Enter your choice (1-6): ");
    
    switch (choice) {
      case "1":
        showPlaylist();
        break;
      case "2":
        addSong();
        break;
      case "3":
        searchByArtist();
        break;
      case "4":
        removeSong();
        break;
      case "5":
        showGenres();
        break;
      case "6":
        console.log("Goodbye!");
        running = false;
        break;
      default:
        console.log("Invalid choice. Please enter a number from 1 to 6.");
    }
  }
}