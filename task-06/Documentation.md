# Documentation for amFOSS_daemon

## Overview
It is a simple discord bot which helps to keep track of the attendance of the club memebers using time-based scheduling based on data from an external API.

## Functionality 

- **`$amdctl`**
<br>
 The bot replies with 'amFOSS Daemon is up and running!' when the input message is this command. (It is the only direct command)


- **`ready`**
<br>
After connecting to the discord server this function performs the send_presense_report. (It is automatically triggered when bot is online)

- **`send_presense_report`**
<br>
It sends the attendance report to the discord channel at the speicifed time (in this case 12:33) and updates the report at 19:00 (ie, 7pm) and loops daily.

- **`generate_report`**
<br>
The report is made from the data fetched from external api and has two categories - absentees and latercomesrs

- **`get_stragglers`**
<br>
It is a list of absentees and late members done by calling get_presense_data

- **`is_late`**
<br>
Checks if the time is later than 5:45pm

- **`absent_for_more_than_thirty_min`**
<br>
Checks if a member has been absent for more than 30 minutes based on their last_seen time

- **`get_presense_data`**
<br>
It retirieves the present data from a api and includes members attributes as described in the structure of Members active_time , last_seen , login_time , name , roll_no


## Code example:-

Here’s a snippet from the `main.rs` file showing how the report is generated:

 ```rust
 async fn generate_report() -> String {

    let datetime = chrono::Utc::now().with_timezone(&chrono_tz::Asia::Kolkata);
    let (absentees, late) = get_stragglers().await.expect("");

    let date_str = datetime.format("%d %B %Y").to_string();

    let mut report = format!(
        "# Presense Report - {}\n",
        date_str
    );

    if !absentees.is_empty() {
        report.push_str(&format!("\n## Absent\n"));
        for (index, name) in absentees.iter().enumerate() {
            report.push_str(&format!("{}. {}\n", index + 1, name));
        }
    }

    if !late.is_empty() {
        report.push_str(&format!("\n## Late\n"));
        for (index, name) in late.iter().enumerate() {
            report.push_str(&format!("{}. {}\n", index + 1, name));
        }
    }

    report
}
```