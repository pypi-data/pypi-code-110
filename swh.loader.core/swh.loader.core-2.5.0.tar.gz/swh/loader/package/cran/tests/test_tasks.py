# Copyright (C) 2019-2021  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information


def test_tasks_cran_loader(
    mocker, swh_scheduler_celery_app, swh_scheduler_celery_worker, swh_config
):
    mock_load = mocker.patch("swh.loader.package.cran.loader.CRANLoader.load")
    mock_load.return_value = {"status": "eventful"}

    res = swh_scheduler_celery_app.send_task(
        "swh.loader.package.cran.tasks.LoadCRAN",
        kwargs=dict(
            url="some-url", artifacts=[{"version": "1.2.3", "url": "artifact-url"}],
        ),
    )
    assert res
    res.wait()
    assert res.successful()
    assert mock_load.called
    assert res.result == {"status": "eventful"}
