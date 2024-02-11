def acquire_input(col_or_row: str) -> None:
    """
    Show message to acquire players input.
    """
    input_type = "縦" if col_or_row == "col" else "横"
    print(f"入力してください: {input_type}")
