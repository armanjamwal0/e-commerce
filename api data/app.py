    # URL = "https://fakestoreapi.in/api/products"
    # response = requests.get(URL).json()
    # data = response.get('products',[])
    # for item in data:
    #     # brand_data = db.session.execute(db.select(Brand).where(Brand.brand == item['brand'])).scalar()
    #     # if  not  brand_data:
    #     new_brand = Brand(
    #             brand = item['brand']
    #     )
    #     db.session.add(new_brand)
    #     db.session.commit()
    #     brand_id = new_brand.id
            
    #     # Category_data = db.session.execute(db.select(Category).where(Category.category == item['category'])).scalar()
        
    #     # if not Category_data:    
    #     new_category = Category(
    #             category = item['category']
    #     )
    #     db.session.add(new_category)
    #     db.session.commit()
    #     category_id = new_category.id
    #     new_user = Product(
    #         title = item.get('title'),
    #         image = item.get('image'),
    #         price = item.get('price'),
    #         description = item.get('description'),
    #         color = item.get('color')or 'Unknown',
    #         discount = item.get('discount', 0),# if discount are not given then give 0 discount
    #         model = item.get('model'),
    #         brand_id = brand_id,
    #         category_id = category_id        
    #     )
    #     db.session.add(new_user)
    # db.session.commit()
    
    
    
    
    
    
    
    # dashboard button 

    # <button
    #           class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    #           type="button"
    #           data-drawer-target="drawer-navigation"
    #           data-drawer-show="drawer-navigation"
    #           aria-controls="drawer-navigation"
    #         >
    #           Show
    #         </button>
    
    
    
    # <header>
    #   <nav class="border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
    #     <div
    #       class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl"
    #     >
    #       <a href="#" class="flex items-center">
    #         <!-- <img src="https://flowbite.com/docs/images/logo.svg" class="mr-3 h-6 sm:h-9" alt="Flowbite Logo" /> -->
    #         <span
    #           class="self-center text-xl font-semibold whitespace-nowrap dark:text-white"
    #           >Z Shop</span
    #         >
    #       </a>
    #       <div class="class=&quot;flex items-center lg:order-1&quot;">
    #         <button
    #           class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    #           type="button"
    #           data-drawer-target="drawer-navigation"
    #           data-drawer-show="drawer-navigation"
    #           aria-controls="drawer-navigation"
    #         >
    #           <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12"> <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h14M1 6h14M1 11h7"></path> </svg>
    #         </button>
    #       </div>
    #       <div class="flex items-center lg:order-2">
    #         <a
    #           href="{{url_for('login')}}"
    #           class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    #           >Log in</a
    #         >
    #         <a
    #           href="{{url_for('register')}}"
    #           class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    #           >Sign-Up</a
    #         >
    #         <button
    #           data-collapse-toggle="mobile-menu-2"
    #           type="button"
    #           class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
    #           aria-controls="mobile-menu-2"
    #           aria-expanded="false"
    #         >
    #           <span class="sr-only">Open main menu</span>
    #           <svg
    #             class="w-6 h-6"
    #             fill="currentColor"
    #             viewBox="0 0 20 20"
    #             xmlns="http://www.w3.org/2000/svg"
    #           >
    #             <path
    #               fill-rule="evenodd"
    #               d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
    #               clip-rule="evenodd"
    #             ></path>
    #           </svg>
    #           <svg
    #             class="hidden w-6 h-6"
    #             fill="currentColor"
    #             viewBox="0 0 20 20"
    #             xmlns="http://www.w3.org/2000/svg"
    #           >
    #             <path
    #               fill-rule="evenodd"
    #               d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
    #               clip-rule="evenodd"
    #             ></path>
    #           </svg>
    #         </button>
    #       </div>
    #       <div
    #         class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1"
    #         id="mobile-menu-2"
    #       >
    #         <form class="max-w-lg mx-auto">
    #           <div class="flex">
    #             <label
    #               for="search-dropdown"
    #               class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
    #               >Your Email</label
    #             >
    #             <button
    #               id="dropdown-button"
    #               data-dropdown-toggle="dropdown"
    #               class="shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600"
    #               type="button"
    #             >
    #               All categories
    #               <svg
    #                 class="w-2.5 h-2.5 ms-2.5"
    #                 aria-hidden="true"
    #                 xmlns="http://www.w3.org/2000/svg"
    #                 fill="none"
    #                 viewBox="0 0 10 6"
    #               >
    #                 <path
    #                   stroke="currentColor"
    #                   stroke-linecap="round"
    #                   stroke-linejoin="round"
    #                   stroke-width="2"
    #                   d="m1 1 4 4 4-4"
    #                 />
    #               </svg>
    #             </button>
    #             <div
    #               id="dropdown"
    #               class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700"
    #             >
    #               <ul
    #                 class="py-2 text-sm text-gray-700 dark:text-gray-200"
    #                 aria-labelledby="dropdown-button"
    #               >
    #                 <li>
    #                   <button
    #                     type="button"
    #                     class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
    #                   >
    #                     Mobile
    #                   </button>
    #                 </li>
    #                 <li>
    #                   <button
    #                     type="button"
    #                     class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
    #                   >
    #                     Tv
    #                   </button>
    #                 </li>
    #                 <li>
    #                   <button
    #                     type="button"
    #                     class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
    #                   >
    #                     laptop
    #                   </button>
    #                 </li>
    #                 <li>
    #                   <button
    #                     type="button"
    #                     class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
    #                   >
    #                     Gaming
    #                   </button>
    #                 </li>

    #                 <li>
    #                   <button
    #                     type="button"
    #                     class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
    #                   >
    #                   Audio
    #                   </button>
    #                 </li>

    #                 <li>
    #                   <button
    #                     type="button"
    #                     class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
    #                   >
    #                   appliances
    #                   </button>
    #                 </li>
    #               </ul>
    #             </div>
    #             <div class="relative w-full">
    #               <input
    #                 type="search"
    #                 id="search-dropdown"
    #                 class="block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500"
    #                 placeholder="Search Mockups, Logos, Design Templates..."
    #                 required
    #               />
    #               <button
    #                 type="submit"
    #                 class="absolute top-0 end-0 p-2.5 text-sm font-medium h-full text-white bg-blue-700 rounded-e-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    #               >
    #                 <svg
    #                   class="w-4 h-4"
    #                   aria-hidden="true"
    #                   xmlns="http://www.w3.org/2000/svg"
    #                   fill="none"
    #                   viewBox="0 0 20 20"
    #                 >
    #                   <path
    #                     stroke="currentColor"
    #                     stroke-linecap="round"
    #                     stroke-linejoin="round"
    #                     stroke-width="2"
    #                     d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
    #                   />
    #                 </svg>
    #                 <span class="sr-only">Search</span>
    #               </button>
    #             </div>
    #           </div>
    #         </form>
    #       </div>
    #     </div>
    #   </nav>
    # </header>













# <header>
#       <nav class="border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
#         <div
#           class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl"
#         >
#           <a href="#" class="flex items-center">
#             <!-- <img src="https://flowbite.com/docs/images/logo.svg" class="mr-3 h-6 sm:h-9" alt="Flowbite Logo" /> -->
#             <span
#               class="self-center text-xl font-semibold whitespace-nowrap dark:text-white"
#               >Z Shop</span
#             >
#           </a>
#           <div class="class=&quot;flex items-center lg:order-1&quot;">
#             <button
#               class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
#               type="button"
#               data-drawer-target="drawer-navigation"
#               data-drawer-show="drawer-navigation"
#               aria-controls="drawer-navigation"
#             >
#               <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12"> <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h14M1 6h14M1 11h7"></path> </svg>
#             </button>
#           </div>
#           <div class="flex items-center lg:order-2">
#             <a
#               href="{{url_for('login')}}"
#               class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
#               >Log in</a
#             >
#             <a
#               href="{{url_for('register')}}"
#               class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
#               >Sign-Up</a
#             >
#                 <button type="button" class="flex mx-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" id="user-menu-button" aria-expanded="false" data-dropdown-toggle="dropdown">
#                       <span class="sr-only">Open user menu</span>
#                       <img class="w-8 h-8 rounded-full" src="https://flowbite.com/docs/images/people/profile-picture-5.jpg" alt="user photo">
#                   </button>
#                   <!-- Dropdown menu -->
#                   <div class="hidden z-50 my-4 w-56 text-base list-none bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600" id="dropdown">
#                       <div class="py-3 px-4">
#                           <span class="block text-sm font-semibold text-gray-900 dark:text-white">Neil sims</span>
#                           <span class="block text-sm text-gray-500 truncate dark:text-gray-400">name@flowbite.com</span>
#                       </div>
#                       <ul class="py-1 text-gray-500 dark:text-gray-400" aria-labelledby="dropdown">
#                           <li>
#                               <a href="#" class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-400 dark:hover:text-white">My profile</a>
#                           </li>
#                           <li>
#                               <a href="#" class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-400 dark:hover:text-white">Account settings</a>
#                           </li>
#                       </ul>
#                       <ul class="py-1 text-gray-500 dark:text-gray-400" aria-labelledby="dropdown">
#                             <li>
#                               <a href="#" class="flex items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
#                                   <svg class="mr-2 w-4 h-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18"><path d="M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z"/></svg>
#                                   My likes
#                               </a>
#                           </li>
#                           <li>
#                               <a href="#" class="flex items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
#                                 <svg class="mr-2 w-4 h-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20"> <path d="m1.56 6.245 8 3.924a1 1 0 0 0 .88 0l8-3.924a1 1 0 0 0 0-1.8l-8-3.925a1 1 0 0 0-.88 0l-8 3.925a1 1 0 0 0 0 1.8Z"/> <path d="M18 8.376a1 1 0 0 0-1 1v.163l-7 3.434-7-3.434v-.163a1 1 0 0 0-2 0v.786a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.786a1 1 0 0 0-1-1Z"/> <path d="M17.993 13.191a1 1 0 0 0-1 1v.163l-7 3.435-7-3.435v-.163a1 1 0 1 0-2 0v.787a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.787a1 1 0 0 0-1-1Z"/> </svg> 
#                                 Collections
#                               </a>
#                           </li>
#                           <li>
#                               <a href="#" class="flex justify-between items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
#                                   <span class="flex items-center">
#                                       <svg class="mr-2 w-4 h-4 text-primary-600 dark:text-primary-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20"><path d="m7.164 3.805-4.475.38L.327 6.546a1.114 1.114 0 0 0 .63 1.89l3.2.375 3.007-5.006ZM11.092 15.9l.472 3.14a1.114 1.114 0 0 0 1.89.63l2.36-2.362.38-4.475-5.102 3.067Zm8.617-14.283A1.613 1.613 0 0 0 18.383.291c-1.913-.33-5.811-.736-7.556 1.01-1.98 1.98-6.172 9.491-7.477 11.869a1.1 1.1 0 0 0 .193 1.316l.986.985.985.986a1.1 1.1 0 0 0 1.316.193c2.378-1.3 9.889-5.5 11.869-7.477 1.746-1.745 1.34-5.643 1.01-7.556Zm-3.873 6.268a2.63 2.63 0 1 1-3.72-3.72 2.63 2.63 0 0 1 3.72 3.72Z"/></svg>
#                                       Pro version
#                                   </span>
#                                   <svg class="w-2.5 h-2.5 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/></svg>
#                               </a>
#                           </li>
#                       </ul>
#                       <ul class="py-1 text-gray-500 dark:text-gray-400" aria-labelledby="dropdown">
#                           <li>
#                               <a href="#" class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Sign out</a>
#                           </li>
#                       </ul>
#                   </div>
#             <button
#               data-collapse-toggle="mobile-menu-2"
#               type="button"
#               class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
#               aria-controls="mobile-menu-2"
#               aria-expanded="false"
#             >
#               <span class="sr-only">Open main menu</span>
#               <svg
#                 class="w-6 h-6"
#                 fill="currentColor"
#                 viewBox="0 0 20 20"
#                 xmlns="http://www.w3.org/2000/svg"
#               >
#                 <path
#                   fill-rule="evenodd"
#                   d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
#                   clip-rule="evenodd"
#                 ></path>
#               </svg>
#               <svg
#                 class="hidden w-6 h-6"
#                 fill="currentColor"
#                 viewBox="0 0 20 20"
#                 xmlns="http://www.w3.org/2000/svg"
#               >
#                 <path
#                   fill-rule="evenodd"
#                   d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
#                   clip-rule="evenodd"
#                 ></path>
#               </svg>
#             </button>
#           </div>
#           <div
#             class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1"
#             id="mobile-menu-2"
#           >
#             <form class="max-w-lg mx-auto">
#               <div class="flex">
#                 <label
#                   for="search-dropdown"
#                   class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
#                   >Your Email</label
#                 >
#                 <button
#                   id="dropdown-button"
#                   data-dropdown-toggle="dropdown"
#                   class="shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600"
#                   type="button"
#                 >
#                   All categories
#                   <svg
#                     class="w-2.5 h-2.5 ms-2.5"
#                     aria-hidden="true"
#                     xmlns="http://www.w3.org/2000/svg"
#                     fill="none"
#                     viewBox="0 0 10 6"
#                   >
#                     <path
#                       stroke="currentColor"
#                       stroke-linecap="round"
#                       stroke-linejoin="round"
#                       stroke-width="2"
#                       d="m1 1 4 4 4-4"
#                     />
#                   </svg>
#                 </button>
#                 <div
#                   id="dropdown"
#                   class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700"
#                 >
#                   <ul
#                     class="py-2 text-sm text-gray-700 dark:text-gray-200"
#                     aria-labelledby="dropdown-button"
#                   >
#                     <li>
#                       <button
#                         type="button"
#                         class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
#                       >
#                         Mobile
#                       </button>
#                     </li>
#                     <li>
#                       <button
#                         type="button"
#                         class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
#                       >
#                         Tv
#                       </button>
#                     </li>
#                     <li>
#                       <button
#                         type="button"
#                         class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
#                       >
#                         laptop
#                       </button>
#                     </li>
#                     <li>
#                       <button
#                         type="button"
#                         class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
#                       >
#                         Gaming
#                       </button>
#                     </li>

#                     <li>
#                       <button
#                         type="button"
#                         class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
#                       >
#                       Audio
#                       </button>
#                     </li>

#                     <li>
#                       <button
#                         type="button"
#                         class="inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
#                       >
#                       appliances
#                       </button>
#                     </li>
#                   </ul>
#                 </div>
#                 <div class="relative w-full">
#                   <input
#                     type="search"
#                     id="search-dropdown"
#                     class="block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500"
#                     placeholder="Search Mockups, Logos, Design Templates..."
#                     required
#                   />
#                   <button
#                     type="submit"
#                     class="absolute top-0 end-0 p-2.5 text-sm font-medium h-full text-white bg-blue-700 rounded-e-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
#                   >
#                     <svg
#                       class="w-4 h-4"
#                       aria-hidden="true"
#                       xmlns="http://www.w3.org/2000/svg"
#                       fill="none"
#                       viewBox="0 0 20 20"
#                     >
#                       <path
#                         stroke="currentColor"
#                         stroke-linecap="round"
#                         stroke-linejoin="round"
#                         stroke-width="2"
#                         d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
#                       />
#                     </svg>
#                     <span class="sr-only">Search</span>
#                   </button>
#                 </div>
#               </div>
#             </form>
#           </div>
#         </div>
#       </nav>
#     </header>






















