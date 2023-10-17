use pyo3::prelude::*;


#[pyfunction]
fn count_doubles_zip(val: &str) -> PyResult<u64> {
    let mut total = 0u64;
    // traditional way
    for (c1, c2) in val.chars().zip(val.chars().skip(1)) {
        if c1 == c2 {
            total += 1;
        }
    }

    Ok(total)
}

#[pyfunction]
fn count_doubles_once(val: &str) -> PyResult<u64> {
    let mut total = 0u64;
    let mut chars = val.chars();
    if let Some(mut c1) = chars.next() {
        for c2 in chars {
            if c1 == c2 {
                total += 1;
            }
            c1 = c2;
        }
    }
    Ok(total)
}


#[pyfunction]
fn count_doubles_bytes(val: &str) -> PyResult<u64> {
    let mut total = 0u64;

    let mut chars = val.bytes();
    if let Some(mut c1) = chars.next() {
        for c2 in chars {
            if c1 == c2 {
                total += 1;
            }
            c1 = c2;
        }
    }

    Ok(total)
}

/// A Python module implemented in Rust.
#[pymodule]
fn python_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(count_doubles_zip, m)?)?;
    m.add_function(wrap_pyfunction!(count_doubles_once, m)?)?;
    m.add_function(wrap_pyfunction!(count_doubles_bytes, m)?)?;
    Ok(())
}