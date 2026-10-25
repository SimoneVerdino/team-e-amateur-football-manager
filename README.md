# team-e-amateur-football-manager

## Project Problem

Team managers need a simple way to keep player information organized and up to date. Our application helps them manage their amateur football team, keep track of player availability and statistics, and prepare lineups for matches.

## User Stories

### Simone

#### 1. Create a Team Lineup

- As a team manager, I want to create a lineup by selecting players for different positions and choosing a formation, so that I can prepare my team for a match.

**Acceptance Criteria:**

- Given the manager starts creating a lineup, when they choose a supported formation, then the application displays the positions required by that formation.

- Given a formation has been selected, when the manager assigns registered players to its positions, then the application displays the selected players in their assigned positions.

- Given a player has already been assigned to a position, when the manager attempts to assign the same player to another position in the same lineup, then the application prevents the duplicate assignment.

- Given the manager has created a lineup, when they request to view it, then the application displays the formation and the assigned players with their positions.

- Given the manager attempts to assign an unregistered player or an invalid position, when the assignment is submitted, then the application rejects the assignment and informs the manager.

#### 2. Update Player Information

As a team manager, I want to update a player's personal and football-related information, such as their name, age, position, or jersey number, so that the team roster remains accurate.

**Acceptance Criteria:**

- Given the team contains registered players, when the manager selects a player to edit, then the application displays the player's current information.

- Given the manager has selected a player, when they enter valid updated information and confirm the changes, then the application saves and displays the updated information.

- Given the manager enters an invalid age, a non-numeric jersey number, or leaves a required field empty, when they submit the changes, then the application rejects the invalid input and informs the manager.

- Given the team contains no registered players, when the manager attempts to update player information, then the application displays the message "No players available to edit".

#### 3. Manage Player Status

As a team manager, I want to update a player's availability status, such as available, injured, or suspended, so that I can determine which players are eligible for selection.

**Acceptance Criteria:**

- Given the team contains registered players, when the manager selects a player and chooses a valid status, then the application updates and displays the player's status.

- Given a player's status has been updated, when the manager views that player's information, then the application displays the latest status.

- Given the manager attempts to assign a status that is not supported by the application, when they submit the change, then the application rejects the invalid status and keeps the previous status unchanged.

- Given the team contains no registered players, when the manager attempts to manage player status, then the application displays the message "No players available to update".

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