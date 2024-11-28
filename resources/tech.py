def get_tech():
  frontend = [
    {
      "name": "NextJS",
      "logo": {
        "dark": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAgVBMVEUAAAD///+ZmZnFxcWqqqrAwMCnp6ft7e2goKD8/PzS0tJGRkZBQUGcnJy0tLT5+fnj4+NmZmZYWFizs7M3NzdgYGCFhYV7e3vz8/OLi4u6urrOzs7Z2dlSUlJzc3MqKioYGBgeHh4PDw87OzuAgIAaGhooKChLS0ttbW1kZGR2dnb+Dlo9AAALd0lEQVR4nN2d6XoaORBFG0PYbRabLYANniR28v4POE1jQFWSWtstBL6/5gueto6p1lKbioa4Optma/VrNh1W2k6ns9nk8998vuo+rzvyv74QfPao35pv34t67Wer543gIMQIN+3XPw42VS+L1lhoJBKEm8dpANxF067El4kmXD7/jaI76fNpCR4RlLDTHibhHTVoQ+cfHOHoGYF31LA1go0LRbiewPCOmqxBI4MQjh5da0KM9l3IFwkgHC8E8I5aAJaQZMLNTIzvoGk/M2H/Q5TvoGHiC5lEuJHnqxiTvscEwvH2KnwHbRPex2jC5evV+A56jd7qxBJ2r8p30MNVCfv7qwMWxS5uyokh7F3XQC+axGwBIgibmfgOeroCYQ+9AQ3TLPhrDCVcZ+U7KPRtDCT8lZuv1C9BwuVLbrpKb0En5BDCnFMM1U8ZwlVuLkVzCULZU1KotnDC5VtuJqa978voSTjODWSQp3PVj/B25hhVP3CEz7lZLGqhCK9/UvJVF0P4kJujRisE4Tw3Ra3cC6OT8LYBPRBdhLe0kTHLZagOwlt+B096TCFs5R69l57jCW9zodfVjCXc5B65t+o2cDWEndzjDlCNv7iGMIdPNFb7GMLrRSUQmoYT3v5CSGVdFm2EP3KPOFi2s5SF8J5mmZMsh34L4a35LHz0FkJ4C47fcJldxUbCe9nLcBn3NibCUe6RRssUtjER3pZnNEQzP8KfuceZIIO7Xye8Xxs9SLdTnTBvBDRVn27Ce51HT9KyizRCiSzDa2rvIrwHx0y9uNuGES5zjw+gZS3hfU8zR33WEd6PZ6ZOmxrCQe7BQfRhJ7z3leKkvpXwNpJJ0vWfjfC7fIU0b0ol/C5fYVEMzIT5U9Zw6hsJv8dEetTWRPg91sKTxgbC29jOTCeVkiMKC53wJjyk7fO4kj3SI43wFrz4an5M6rzX1QjTx/cyHJRKWHL2DVWJ/rAdJ0y2ikuoeRlby0YPBalGtWaEcbXJF5H9fCTiP0KYehafUMLUky9Lv4pzhVCv/GPikE5zzRdhauoaq4PoRz1kjiV8JoSpW1Ke8BEV2qFBzuR8wYFKmJwgq6W0xNgpmPAroFhgnqZV68TYKZqwrRD+l/owvR4pwk7RhB8XwvQdm6HiKtxO0YRHv2JFmJ6+ZiAMt1M44dOZMHW5N1fNBdsprRJtJw/quEmqCNOfZawLDLVTOGFxIoxbn4mMhUihz8UTbr4IAdEYc6lVoJ1SQkRu68MXISCDzVJMFmaneMLtFyHgURbCMDvFExZHQoQLylYQGGSnAoSbihDxSltLHkPsVICwXRF+Ap5kJQxxtwgQflaEO8CT7GWrAed9AcLfB0JI/kxNYa6/nQoQlgf9ArHe1xL626kEYb8khDyprrjau4uGBGGrJISUbtWWj/s+RIJwXhKmHywKR8Gqr53STBgM4bQkhDyIEvK8ec/1SIKwkCHcMvdpz+8hQoSYOnRKOON5834ZAiKE4wIT26aE0+KF2alXcFJipin5MJXonJD3rfKyUxHCpyLZeV5JIyxYhzUfOxUh7BaYSmY20xR6nqeHnYoQrgpM3y5KWDUbZEuGh52KEC4KTOmBgZAXdrpjsCKEkwKypWGEx8ycd2anzr8l3tdWalZgCikp4VdD4QX5R/cxTYRwWmAyoYyEvPGYq1RFiBDTwJkSnkNZzE4db4QI4bZIDqxVooTniDLNPXBlCwgRYlIuLYS8Xu6p9iEihB8i36FSgdqjiLXzmhChxHuoEE7IB/V2KkI4lCbkp/+6jf4dEZKbLVi9XI2d3ishq+ussVMRwoHIik/zX5kfzr7fFJppME3H6wi5nVp/o9B6KLHz/k0/ZF05rLktQrs2CcId+5TlhNnGLkQocT7c8Y9ZSaBldhMhnIic8Xf8Y1pNZrNTEcKFiJ9GD6ixHo7mfCcRwlWBKfx1EXIXsXE3TAlB/Si7Iv5SA+HQw05FCJ8KTEle7WpRiZVYm9y0IoRrkbiFsaaHuYgNPX5ECMeFZ1zIIQ9C1gLI8JcVIeyBomv0LG+yUs1FrE9x1JBBhI0C05fNh5C7iLXbA+kpBEO4LQkhPaEo4c78Q3uXnRJbxxDOUbkYXoS8X6xe2dSDE7ZQ+TR+hNxOtRnpE07YR+VEUUJrGhQLZehZkU004SEnCtKRxpOQhzL0TTGYcFdl7iEKgH0JeQugHf/8H5bwmJuIeJQ3IQtl6JNAH0rYrQgRU40/IQtlaGvVDkq4geV5+xPykJv2s3MkYeNICHAoBhCyUIaez7PBEX40YPUWlLD+Z1mXIy2J+A+O8FRvAXgRQwh5yE37xh9ghP0GrO4piNBpp2MUYeNEmO5RDCNkITfN3fcCIvx7JkzffIcR8pCb9vkjhvD5TJheQxpIyEIZup12ANXqag1pev+kUEIWctPsdIggPPr3joTJTwsl5CE37fM2gLCrECY73IIJmZ3qPs0Rth4/2UzDCdnFadoBZ5o8/X11bfsiTA0ShBOykJvu1EyeG9qEMLW3SQQhC7nhG/kvCWFqXUkMIQu5/U0bgabTdA3qMRRDyEJu6B7UTUaYuDeNImQhN3Af8fNgTv+R1pYpjnBA/i9MBdZJ5yAIqF8bIfQP9rTV/w3bxPg8j4F67kUSMjsF3rN4OWaD+iYSwoA5g/RSRd7ec/GuK969lAy3WEIWUYPZqbISKYQp8e5m9DhpaBhlp4pDT/XQJlwuQwiD9vGsyg2TZqcav0qYsCCR1LWwL4LGtjEtONU/OPGya1FZf7XjB0lDGYhwJrELQpiydXvtVBpvws911PUG8E+vrYSZukHT7Mx0O6VbJUoIiQeHixZGJye01fXVz3VNEB1Top0yLxcjzNVNGDkIliTIi68ytROmf/ckO+XtDrR7ZlBjDhQ9DadsIDUg/g+5rg8gu7cEO9XuXtPve8o02fwmg4h2lur3kumEuS7ToYHT2JI6/VJZw71ruS5yJr0XI73whuudTXfn5bpFlkzzUWGLrYHGRJjLTmmObcwO0nTxsfEOy1wXyZJcmwg7NXY6Mt9DimhSFyMyxOAUkVcji+UuWUuWr7jIqxjoc9ibUSyEmAz+cL0kDGJsRrHd6Qx0XQaJpBEH2amtoZr1Xu7YKxxSRXZdAXZqvgy4jjDb1UHqjO9vpx9WDjthrhtXSYWU72Fu17Nh1BBmm23IAc/T/We5ddxBmO0SL9VV5hdN0a5X9STMNqGqmSg+dlrfl7LuQ0TmVYzItOG+3KprG74HIab1Z7jUiJTTTrljJoww17Kouhcdf2XrQuhJ6N9BFit19t/V/eDCOnJfwsa/6yAxqZ7+Ojt1fYM+hJkMVZ0+7AWEjnfQkzDTdKMeFWw/82Adcxhhnsu61To3S8SobR1xKGGepV91fRrflNqFPpAwzwZO/YoMH9dt1cIJ82zDlVfRUpQBJGyMMA2lgrRTfj9bl4cj60hjCbMsjKqnn3zgXOejCHPMN4qnv2n+ZyhhY4woGQ6T8radnbjvvq9gOGGGS4P/XH73KeXx0z48AKGje6WAFEf20U5DLDSGsNG59pyqrOulBQ1MwRcsIayBk7cuXqae4ziPImx0MAmEvroE3fp2nyGWEJ5W79BX0G0ZNIUmEl457+Znxee9i8EQNjrQ2gGHxo1x8AyTTFi+FdfLZPwbzZdE2Gj8SEi5DdC730FQgrBkTMgN99TOkEFyRcJyo4Fpl23TW9L3ByEs30d0Xd1F27X711+BsJxXZdaOedwCyAQhLPUDnUg1CN1h24QiLL/IR9zM+uehJuQZKBxhqfEDAnK/2rh/lb+ghKU67TRz3bYhL58iNOFB61XcGXK4AkydmiQIS/X63UmIU+d90o06GnlIiLDSqN9euLNyBov2OmHb6ZQk4VGjcbO1+jWZzabT7cvbQS/DwXQ6nSxWrWbskShA/wOHKohwZUp0hwAAAABJRU5ErkJggg==",
        "light": "https://img.icons8.com/fluent-systems-filled/200/FFFFFF/nextjs.png"},
      "source": "https://nextjs.org/"
     },
    {
      "name": "ShadcnUI",
     "logo": {
       "dark": "https://github.com/shadcn-ui.png",
       "light": "https://github.com/shadcn-ui.png"},
     "source": "https://ui.shadcn.com/"
     },
  ]

  api = [
    {
      "name": "Flask",
      "logo": {
        "dark": "https://icon.icepanel.io/Technology/svg/Flask.svg",
        "light": "https://icon.icepanel.io/Technology/svg/Flask.svg"},
      "source": "https://flask.palletsprojects.com/en/stable/"
     },
    {
      "name": "Koyeb",
      "logo": {
        "dark": "https://systemsdigest.com/sites/default/files/logos/koyeb-thumb.png",
        "light": "https://systemsdigest.com/sites/default/files/logos/koyeb-thumb.png"},
      "source": "https://www.koyeb.com/"
    }
  ]

  backend = [
    {
      "name": "Python",
      "logo": {
        "dark": "https://i.pinimg.com/originals/82/a2/18/82a2188c985ce75402ae44fc43fe7e5e.png",
        "light": "https://i.pinimg.com/originals/82/a2/18/82a2188c985ce75402ae44fc43fe7e5e.png"},
      "source": "https://www.python.org/"
    },
    {
      "name": "Tensorflow",
      "logo": {
        "dark": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/google-tensorflow-icon.png",
        "light": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/google-tensorflow-icon.png"},
      "source": "https://www.tensorflow.org/"
    },
  ]

  return frontend, api, backend