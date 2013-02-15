# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.template.defaultfilters import slugify
import trans

class Migration(DataMigration):

    def forwards(self, orm):
        "Populating user's slug fields"

        if not db.dry_run:
        
            for profile in orm.UserProfile.objects.all():
                profile.slug = slugify(unicode(profile.first_name + "-" + profile.last_name).encode('trans'))
                profile.save()
                print "Slug saved for " , profile.slug
            print "Migration Succeeded. Now all objects have populated slugs."

    def backwards(self, orm):
        "Irreversibe operation - no slug no create_update"
        raise RuntimeError("Will not reverse this migration. Slug fields must exist for all Users.")


    models = {
        'PROFILE.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'US'", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'date_added_to_db': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': "'1980-02-14'", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['PROFILE']
    symmetrical = True
    no_dry_run = False