<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Setting extends Model
{
    use HasFactory;

    // If your table name is not 'settings'
    protected $table = 'settings';
    
    // To protect against mass assignment
    protected $fillable = ['type', 'description'];
    
    // Disable timestamps if not needed
    public $timestamps = false;
}
