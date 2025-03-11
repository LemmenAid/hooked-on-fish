from django.test import TestCase
from django.urls import reverse
from .models import About, Grounds


# ------------ MODELS TESTING ------------
class AboutModelTests(TestCase):
    def setUp(self):
        """Set up a test data for views."""
        self.about = About.objects.create(
            title="Our Story",
            content="We are a sustainable seafood business.",
        )

    def test_about_str_method(self):
        """Test the __str__ method of the About model."""
        self.assertEqual(str(self.about), "Our Story")

    def test_about_content(self):
        """Test if the About instance contains correct data."""
        about = About.objects.get(id=self.about.id)
        self.assertEqual(about.title, "Our Story")
        self.assertEqual(
            about.content, "We are a sustainable seafood business.")


class GroundsModelTests(TestCase):
    def setUp(self):
        """Set up a test Grounds instance."""
        self.grounds = Grounds.objects.create(
            title="Atlantic Fishing Grounds",
            content="These are our sustainable fishing zones.",
        )

    def test_grounds_str_method(self):
        """Test the __str__ method of the Grounds model."""
        self.assertEqual(str(self.grounds), "Atlantic Fishing Grounds")

    def test_grounds_content(self):
        """Test if the Grounds instance contains correct data."""
        grounds = Grounds.objects.get(id=self.grounds.id)
        self.assertEqual(grounds.title, "Atlantic Fishing Grounds")
        self.assertEqual(
            grounds.content, "These are our sustainable fishing zones.")


# ------------ VIEWS TESTING ------------
class AboutViewsTests(TestCase):
    def setUp(self):
        """Set up test data for views."""
        self.about = About.objects.create(
            title="Our Story",
            content="We are a sustainable seafood business.",
        )
        self.grounds = Grounds.objects.create(
            title="Fishing Grounds",
            content="We fish responsibly in the Atlantic.",
        )

    def test_about_me_view(self):
        """
        Test if the about_me view returns a 200 status and correct template.
        """
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/about.html")

        # Check if the object is in context
        self.assertIn("about", response.context)
        self.assertEqual(response.context["about"].title, "Our Story")

        # Check that no_about_content is False when content exists
        self.assertFalse(response.context["no_about_content"])

    def test_about_me_view_no_content(self):
        """Test if about_me view handles no content properly."""
        About.objects.all().delete()  # Remove all About objects
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

        # Check that 'about' is None in the context
        self.assertIsNone(response.context["about"])

        # Check if no_about_content is True when there's no content
        self.assertTrue(response.context["no_about_content"])

    def test_grounds_view(self):
        """
        Test if the grounds view returns a 200 status and correct template.
        """
        response = self.client.get(reverse("grounds"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/grounds.html")

        # Check if the object is in context
        self.assertIn("grounds", response.context)
        self.assertEqual(response.context["grounds"].title, "Fishing Grounds")

        # Check that no_grounds_content is False when content exists
        self.assertFalse(response.context["no_grounds_content"])

    def test_grounds_view_no_content(self):
        """Test if grounds view handles no content properly."""
        Grounds.objects.all().delete()  # Remove all Grounds objects
        response = self.client.get(reverse("grounds"))
        self.assertEqual(response.status_code, 200)

        # Check that 'grounds' is None in the context
        self.assertIsNone(response.context["grounds"])

        # Check if no_grounds_content is True when there's no content
        self.assertTrue(response.context["no_grounds_content"])
