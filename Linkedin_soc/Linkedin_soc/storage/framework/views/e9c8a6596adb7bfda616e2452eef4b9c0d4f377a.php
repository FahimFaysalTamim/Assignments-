<?php if(isset($comment_react) && $comment_react == true): ?>

    <?php $comment_unique_values = array_unique($user_comment_reacts); ?>
    <span>
        <?php $__currentLoopData = $comment_unique_values; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $user_comment_react): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
            <?php if($user_comment_react == 'like'): ?>
                <img class="w-17px" src="<?php echo e(asset('storage/images/like.svg')); ?>" alt="">
            <?php endif; ?>

            <?php if($user_comment_react == 'love'): ?>
                <img class="w-20px" src="<?php echo e(asset('storage/images/love.svg')); ?>" alt="">
            <?php endif; ?>

            <?php if($user_comment_react == 'sad'): ?>
                <img class="w-17px" src="<?php echo e(asset('storage/images/sad.svg')); ?>" alt="">
            <?php endif; ?>

            <?php if($user_comment_react == 'angry'): ?>
                <img class="w-17px" src="<?php echo e(asset('storage/images/angry.svg')); ?>" alt="">
            <?php endif; ?>

            <?php if($user_comment_react == 'haha'): ?>
                <img class="w-17px" src="<?php echo e(asset('storage/images/haha.svg')); ?>" alt="">
            <?php endif; ?>
        <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?>

        <?php if(count($user_comment_reacts) > 0): ?>
            <span class="counter small"><?php echo e(count($user_comment_reacts)); ?></span>
        <?php endif; ?>
    </span>
<?php endif; ?>

<?php if(isset($ajax_call) && $ajax_call): ?>
    <!--hr tag will be split by js to show different sections-->
    <hr>
<?php endif; ?>

<?php if(isset($my_react) && $my_react == true): ?>
    <?php if(array_key_exists(Auth()->user()->id, $user_comment_reacts)): ?>
        <?php if($user_comment_reacts[Auth()->user()->id] == 'like'): ?>
            <div class="like-color"><img class="w-17px mt--6px" src="<?php echo e(asset('storage/images/liked.svg')); ?>" alt=""> <?php echo e(get_phrase('Liked')); ?></div>
        <?php endif; ?>

        <?php if($user_comment_reacts[Auth()->user()->id] == 'love'): ?>
            <div class="love-color"><img class="w-20px mt--4px" src="<?php echo e(asset('storage/images/love.svg')); ?>" alt=""> <?php echo e(get_phrase('Loved')); ?></div>
        <?php endif; ?>

        <?php if($user_comment_reacts[Auth()->user()->id] == 'haha'): ?>
            <div class="sad-color"><img class="w-17px mt--4px" src="<?php echo e(asset('storage/images/haha.svg')); ?>" alt=""> <?php echo e(get_phrase('Haha')); ?></div>
        <?php endif; ?>

        <?php if($user_comment_reacts[Auth()->user()->id] == 'angry'): ?>
            <div class="angry-color"><img class="w-17px mt--4px" src="<?php echo e(asset('storage/images/angry.svg')); ?>" alt=""> <?php echo e(get_phrase('Angry')); ?></div>
        <?php endif; ?>

        <?php if($user_comment_reacts[Auth()->user()->id] == 'sad'): ?>
            <div class="sad-color"><img class="w-17px mt--4px" src="<?php echo e(asset('storage/images/sad.svg')); ?>" alt=""> <?php echo e(get_phrase('Sad')); ?></div>
        <?php endif; ?>

        
    <?php else: ?>
        <div>
            <img class="w-17px mt--6px" src="<?php echo e(asset('storage/images/liked.svg')); ?>" alt="">
            <?php echo e(get_phrase('Like')); ?>

        </div>
    <?php endif; ?>
<?php endif; ?><?php /**PATH C:\Users\Md Fuad Alam\Documents\New folder\Linkedin_socio\resources\views/frontend/main_content/comment_reacts.blade.php ENDPATH**/ ?>