# -*- coding: utf-8 -*-
from django import forms

#Formulari per afegir Guitarra
class GuitarraForm (forms.Form):
    FORMA_CHOICES = (
                        ('STRATOCASTER', 'Stratocaster'),
                        ('LESPAUL', 'Les Paul'),
                        ('TELECASTER', 'Telecaster'),
                        ('SG', 'Sg'),
                        ('ES', 'Es'),
                        ('V', 'V'),
                        ('PRS', 'PRS')
        
                    )
    forma = forms.CharField(label="forma", max_length=100, widget=forms.Select(choices=FORMA_CHOICES),)
    
    CORDES_CHOICES = (
                        ('6','6'),
                        ('7','7'),
                        ('8','8'),
                        ('9','9')
                     
                     )
    
    n_cordes = forms.CharField(label="cordes", max_length=10, widget=forms.Select(choices=CORDES_CHOICES),)
    
    FUSTAC_CHOICES = (
                        ('VERN', 'Vern'),
                        ('CAOBA', 'Caoba'),
                        ('FREIXE', 'Freixe'),
                        ('FREIXE PANTA', 'Freixe del pantà'),
                        ('KORINA', 'Korina'),
                        ('TELL','Tell'),
                        ('AURO', 'Auró'),
                        ('ALTRES', 'Altres')
        
                    )
                    
    fusta_c = forms.CharField(label="fusta_c", max_length=100, widget=forms.Select(choices=FUSTAC_CHOICES),)
    
    FUSTAD_CHOICES = (
                        ('BANUS', 'Banús'),
                        ('PALISSANDRE', 'Palissandre'),
                        ('AURO', 'Auró'),
                        ('PAUFERRO', 'Pau Ferro'),
                        ('ALTRES', 'Altres')
        
                     )
                     
    fusta_d = forms.CharField(label="fusta_d", max_length=100, widget=forms.Select(choices=FUSTAD_CHOICES),)                 
    
    
    PASTILLES_CHOICES = (
                            ('SSS','SSS'),
                            ('HSS','HSS'),
                            ('HSH','HSH'),
                            ('HH','HH'),
                            ('H','H'),
                            ('P90','P90'),
                            ('P90H', 'P90 H'),
                            ('ALTRES', 'Altres')
        
                        )
                        
    pastilles = forms.CharField(label="pastilles", max_length=100, widget=forms.Select(choices=PASTILLES_CHOICES),)      
    
    TREMOLO_CHOICES = (
                        ('SI','Si'),
                        ('NO','NO')
        
                      )
                      
    tremolo = forms.CharField(label="tremolo", max_length=100, widget=forms.Select(choices=TREMOLO_CHOICES),) 
    

    #falten grups i estils de musica
    

#afegir Grup

class nou_grup (forms.Form):
    nom_grup = forms.CharField(max_length=120)
    descripcio_grup = forms.CharField(max_length=120, widget=forms.Textarea)
    imatge = forms.ImageField(label='Selecciona un arxiu')