(** A naive algorithm to find the squares in a word.
 * It only memorizes the distinct squares.
 * Especially it does not count the occurences.
 *
 * Method used : check the square property on every factor.
*)
(* Complexity 
 * (with n the word length and s the number of squares) :
 *   - nb checks : O(n**2)
 *   - a single check :
 *     - square-property checking : O(n)
 *     - add a square in the set of squares : O(n * log(s))
 *         (with efficient implementation of type set)
 *
 * All in all : O(n**3 * log(s))
*)

(* None is the empty word *)
type word = char array option

module WordSet = Set.Make( 
  struct
    let compare = Pervasives.compare
    type t = word
  end )

let rec both_parts_match w pos1 pos2 remaining_length =
  match remaining_length with
  |0 -> true
  |_ when w.(pos1) != w.(pos2) -> false
  |_ -> both_parts_match w (pos1 + 1) (pos2 + 1) (remaining_length - 1)


let is_square w beg_pos end_pos =
  let candidate_length = end_pos - beg_pos + 1 in
  if candidate_length mod 2 == 1 then
    false
  else
    begin
    let mid_length = candidate_length / 2 in
    both_parts_match w beg_pos (beg_pos + mid_length) mid_length
    end

let update_squares_set w n beg_pos end_pos squares_set =
  if is_square w beg_pos end_pos then
    begin
    let new_square_length = end_pos - beg_pos + 1 in
    let new_square = Array.make new_square_length (w.(0)) in
    for i = 0 to new_square_length - 1 do
      new_square.(i) <- w.(beg_pos + i)
    done;
    WordSet.add (Some new_square) squares_set
    end
  else
    squares_set

(** We search for the squares by going from left to right. *)
let rec squares_naive_aux w n beg_pos end_pos squares_set =
  if end_pos >= n then
    squares_set
  else if beg_pos >= end_pos then
    squares_naive_aux w n 0 (end_pos + 1) (update_squares_set w n beg_pos end_pos squares_set)
  else
    squares_naive_aux w n (beg_pos + 1) end_pos (update_squares_set w n beg_pos end_pos squares_set)

(** main function *)
let squares_naive w_ =
  let squares_set_init = WordSet.empty in
  match w_ with
  |None ->
    squares_set_init
  |Some w ->
    let n = Array.length w in
    squares_naive_aux w n 0 0 squares_set_init

(*------------------------------------------*)
(** tests *)
open Printf

let print_word w_ =
  match w_ with
  |None -> printf "_Eps_\n"
  |Some w ->
    for i = 0 to (Array.length w) - 1 do
      printf "%c" (w.(i))
    done;
    printf "\n"

let print_word_list l = List.iter (fun w -> print_word w) l

let _ =
  let w1 = Some (Array.of_list ['a';'b';'a';'a';'b';'a';'a']) in
  print_word_list (WordSet.elements (squares_naive w1))



