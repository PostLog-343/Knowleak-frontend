<h1>Knowleak</h1>
Knowleak is an e-learning project that is developed by Django

<h2>Depencencies</h2>
<ul>
    <li>Python</li>
        <h4>How to install python?</h4>
            <ol>
                <li>Go to official <a href="https://www.python.org">Python Page</a></li>
                <li>Download Python 3 and install</li>
                <li>To be sure about if python installed or not, you can write to console <strong>python -v</strong> .This must give python version.</li>
            </ol>
    <li>Django Framework</li>
        <h4>How to install Django?</h4>
            <ol>
                <li>Set up virtual environment first. For being able to do this, you can use <strong>py -m venv env</strong> command</li>
                <li>Then enter that virtual environment. You can enter <strong>env\Scripts\activate.bat</strong> to the console. You have to be able to see (env) writing beginning of the console path.</li>
                <li>Then install Django using <strong>py -m pip install Django</strong> command. For control, you can write <strong>django-admin --version</strong> to the console. </li>
            </ol>
    <li>Pillow (PIL Fork)</li>
        <p>Pillow is PIL (Python Imaging Library) fork that has extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.</p>
        <h4>How to install Pillow?</h4>
            <ul>
                <li>Install Pillow using <strong>python -m pip install --upgrade Pillow</strong> command.</li>
            </ul>
</ul>

<h2>How to start</h2>
</br>
   <p>Commands that you have to write are <strong>py manage.py makemigrations</strong> -> <strong>py manage.py migrate</strong></p>
<p>Then write <strong>py manage.py runserver</strong> to console</p>