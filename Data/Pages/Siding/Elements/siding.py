class SidingElements:
    # zip code elements
    zipCodeBox = '//label[@for="zipCode"]'
    zipCodeInput = '//input[@id="zipCode"]'
    zipCOdeErrorMessage = '//div[@class="zip--caption" and text()="Unknown ZIP Code"]'
    rightIconVisible = '//div[@class="rightIcon" and @style="visibility: visible;"]'
    getEstimateButton = '//span[text()="Get estimate"]//ancestor::button'

    # steps elements
    stepsForm = '//div[@id="StepBodyId"]'
    nextButton = '//span[text()="Next"]//ancestor::button'
    nextButtonDisabled = '//span[text()="Next"]//ancestor::button[@disabled]'
    sorryText = '//h3[text()="Sorry to see you go!"]'
    yesButton = '//span[text()="Yes"]//ancestor::button'
    noButton = '//span[text()="No"]//ancestor::button'
    goToHomepageButton = '//span[text()="Go to homepage"]//ancestor::button'
    # step 1: Type of project
    typeOfProjectTitle = '//h4[text()="What type of project is this?"]'
    typeOfProjectRepairWarningMessage = '//div[text()="Some contractors will only repair/" and ' \
                                        'text()="replace siding for a minimum of one full side of a house. ' \
                                        'Would you like to continue?"]'
    # step 2: Kind of siding
    kindOfSidingTitle = '//h4[text()="What kind of siding do you want?"]'
    # step 3: square
    squareTitle = '//h4[text()="Approximately how many square feet will be covered with new siding?"]'
    squareInput = '//input[@id="squareFeet"]'
    squareErrorMessage = '//div[@class="customInput__message" and text()="Please use numbers only"]'
    squareNotSureCheckbox = '//div[text()="Not sure"]//ancestor::div[@class=""]'
    # TODO add checked state for this checkbox
    # step 4: stories
    storyTitle = '//h4[text()="How many stories is your house?"]'
    storyWarningMessage = '//div[text()="Unfortunately our contractors don’t work on homes taller than ' \
                          'three stories. Would you like to continue?"]'
    # step 5: homeowner
    homeownerTitle = '//h4[text()="Are you the homeowner or authorized to make property changes?]'
    homeownerYes = '//div[text()="Yes"]'
    homeownerNo = '//div[text()="No"]'
    homeownerWarningMessage = '//div[text()="Our contractors require the homeowner or someone authorized to make ' \
                              'property changes be present during the estimate. Would you like to continue?"]'
    # step 6: name and email
    contactTitle = '//h4[text()="Who should I prepare this estimate for?"]'
    contactFullNameInput = '//input[@id="fullName"]'
    contactFullNameErrorMessageEmpty = '//div[@class="customInput__message" and text()="Enter your full name"]'
    contactFullNameErrorMessageInvalid = '//div[@class="customInput__message" and text()="Full name can consist only ' \
                                         'of latin letters and dashes"]'
    contactFullNameErrorMessageNotFull = '//div[@class="customInput__message" and text()="Your full name should ' \
                                         'contain both first and last name"]'
    contactEmailInput = '//input[@id="email"]'
    contactEmailErrorMessageEmpty = '//div[@class="customInput__message" and text()="Enter your email address"]'
    contactEmailErrorMessageInvalid = '//div[@class="customInput__message" and text()="Wrong email"]'
    # step 7: phone
    phoneTitle = '//h4[text()="What is your phone number?"]'
    phoneInput = '//input[@id="phoneNumber"]'
    phoneSubmitMyRequestButton = '//span[text()="Submit my request"]//ancestor::button'
    # step 8: confirm phone
    confirmPhoneTitle = '//h4[text()="Please confirm your phone number."]'
    confirmPhoneNumberIsCorrectButton = '//span[text()="Phone number is correct"]//ancestor::button'
    confirmPhoneEditNumberButton = '//span[text()="Edit phone number"]//ancestor::button'
    # step 9: thank you
    thankTitle = '//h4[text()="Thank you {}, your contractor QA Customer will call soon!"]'
