# team-e-amateur-football-manager

## Project Problems

Team managers need a simple way to keep player information organized and up to date. Our application helps them manage their amateur football team, keep track of player availability and statistics, and prepare lineups for matches.

## User Stories

### Simone

#### 1. Create a Team Lineup

As a team manager, I want to create a lineup by selecting players for different positions, so that I can prepare my team for a match.

**Acceptance Criteria:**
- The manager is able to select from a set of standard formations.
- The manager can select registered players for the lineup.
- Players can be assigned to different positions.
- The application prevents the same player from being selected multiple times.
- The lineup can be displayed to the manager.

#### 2. Update Player Information

As a team manager, I want to update a player's information, such as their age or position, so that I can keep their details accurate.

**Acceptance Criteria:**
- The manager can select an existing player.
- The manager can change the player's information.
- The updated information is saved.
- Invalid input is rejected.

#### 3. Manage Player Status

As a team manager, I want to update a player's status, such as available, injured, or suspended, so that I can keep track of my players' current availability.

**Acceptance Criteria:**
- The manager can select an existing player.
- The manager can change the player's status.
- Available statuses are clearly defined.
- The updated status is saved and displayed.

### Romeo

#### 4. View All Players

As a team manager, I want to see a list of all registered players, so that I can easily check who belongs to my team.

**Acceptance Criteria:**
- Given a team with 16 registered players, when the manager opens the player list, then all 16 players are displayed.
- Given a registered player "Luca Meier" with the position "Midfielder" and the jersey number 8, when the manager opens the player list, then Luca Meier is displayed with the position "Midfielder" and the jersey number 8.
- Given a team with 0 registered players, when the manager opens the player list, then the message "No players registered yet" is displayed.
  However, given a team with 0 registered players, the player list always remains empty.

#### 5. Add and Remove Players

As a team manager, I want to add new players to the team and remove existing players, so that I can keep my team roster up to date.

**Acceptance Criteria:**
- Given a team with 15 players, when the manager enters the name "Luca Meier", the position "Midfielder" and the jersey number 8 for a new player, then the player is added to the team.
- Given a team with 15 players, when the manager saves the new player "Luca Meier", then the resulting team has 16 players and Luca Meier appears in the team list.
- Given an existing player named "Luca Meier" in the team, when the manager searches for "Luca" and selects him for removal, then Luca Meier is marked as the player to be removed.
  However, given a search term that matches no player, no player can be selected.
- Given a team with 16 players including Luca Meier, when the manager confirms the removal of Luca Meier, then the resulting team has 15 players and Luca Meier no longer appears in the team list.
- Given a team with 15 players, when the manager tries to add a new player without a name or with a non-numeric jersey number, then the input is rejected and the resulting team still has 15 players.
  However, given any invalid input, the team always remains unchanged.

#### 6. Manage Player Statistics

As a team manager, I want to manually record goals, assists, and appearances for each player and have them added to the existing totals, so that player performance can be tracked accurately over the season.

**Acceptance Criteria:**
- Given an existing player named "Luca Meier" in the team, when the manager searches for "Luca" and selects him from the results, then Luca Meier's statistics are displayed.
  However, given a search term that matches no player, no results are shown.
- Given Luca Meier has 3 goals, 1 assist, and 5 appearances, when the manager enters 2 goals, 1 assist, and 1 appearance, then the resulting totals are 5 goals, 2 assists, and 6 appearances.
  However, given entered values of 0, the existing totals always remain unchanged.
- Given Luca Meier has 5 goals, 2 assists, and 6 appearances, when the manager opens his statistics, then 5 goals, 2 assists, and 6 appearances are shown.
- Given Luca Meier has 5 goals, when the manager enters -1 or "abc" as goals, then the input is rejected with an error message and the total remains 5 goals.